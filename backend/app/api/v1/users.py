from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.user import User, Role
from app.schemas.auth import UserRead, UserUpdate, RoleAssignRequest, RoleRead
from app.api.deps import PermissionChecker, get_current_active_user

router = APIRouter(prefix="/users", tags=["User & Role Administration"])

@router.get("", response_model=List[UserRead], dependencies=[Depends(PermissionChecker(["users:read"]))])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

@router.get("/{user_id}", response_model=UserRead, dependencies=[Depends(PermissionChecker(["users:read"]))])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead, dependencies=[Depends(PermissionChecker(["users:write"]))])
def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    for field, val in user_in.model_dump(exclude_unset=True).items():
        setattr(user, field, val)
        
    db.commit()
    db.refresh(user)
    return user

@router.post("/{user_id}/roles", response_model=UserRead, dependencies=[Depends(PermissionChecker(["roles:manage"]))])
def assign_user_roles(user_id: int, role_data: RoleAssignRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    roles = db.query(Role).filter(Role.id.in_(role_data.role_ids)).all()
    user.roles = roles
    db.commit()
    db.refresh(user)
    return user

@router.get("/roles/all", response_model=List[RoleRead], dependencies=[Depends(PermissionChecker(["roles:manage"]))])
def list_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()
