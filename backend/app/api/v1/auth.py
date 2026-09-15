from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.models.user import User, Role, LoginHistory
from app.schemas.auth import UserCreate, UserRead, LoginRequest, Token, PasswordChangeRequest, TokenPayload
from app.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token
from app.api.deps import get_current_user, get_current_active_user
from jose import jwt, JWTError
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["Authentication & Session Management"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_citizen(user_in: UserCreate, db: Session = Depends(get_db)):
    # Check existing email/username
    if db.query(User).filter((User.email == user_in.email) | (User.username == user_in.username)).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists."
        )

    # Create user
    user = User(
        email=user_in.email,
        username=user_in.username,
        hashed_password=get_password_hash(user_in.password),
        full_name=user_in.full_name,
        phone_number=user_in.phone_number,
        is_active=True,
        status="ACTIVE"
    )

    # Assign default CITIZEN role
    citizen_role = db.query(Role).filter(Role.code == "CITIZEN").first()
    if citizen_role:
        user.roles.append(citizen_role)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login", response_model=Token)
def login(request: Request, login_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        (User.email == login_data.username_or_email) | (User.username == login_data.username_or_email)
    ).first()

    ip_address = request.client.host if request.client else "127.0.0.1"

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if user.status == "LOCKED":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account locked due to multiple failed login attempts.")

    if not verify_password(login_data.password, user.hashed_password):
        user.failed_login_attempts += 1
        if user.failed_login_attempts >= 5:
            user.status = "LOCKED"
            log = LoginHistory(user_id=user.id, ip_address=ip_address, status="ACCOUNT_LOCKED")
        else:
            log = LoginHistory(user_id=user.id, ip_address=ip_address, status="FAILED_PASSWORD")
        db.add(log)
        db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # Successful login
    user.failed_login_attempts = 0
    user.last_login_at = datetime.utcnow()
    log = LoginHistory(user_id=user.id, ip_address=ip_address, status="SUCCESS")
    db.add(log)
    db.commit()
    db.refresh(user)

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
        user=user
    )

@router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.post("/refresh", response_model=Token)
def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = TokenPayload(**payload)
        if token_data.sub is None or token_data.type != "refresh":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    user = db.query(User).filter(User.id == int(token_data.sub)).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not active")

    new_access_token = create_access_token(user.id)
    new_refresh_token = create_refresh_token(user.id)
    return Token(access_token=new_access_token, refresh_token=new_refresh_token, token_type="bearer", user=user)

@router.post("/change-password")
def change_password(data: PasswordChangeRequest, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not verify_password(data.current_password, current_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Current password incorrect")
    
    current_user.hashed_password = get_password_hash(data.new_password)
    db.commit()
    return {"message": "Password updated successfully"}
