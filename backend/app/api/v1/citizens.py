from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.citizen import CitizenProfile
from app.schemas.citizen import CitizenProfileCreate, CitizenProfileRead
from app.api.deps import get_current_active_user

router = APIRouter(prefix="/citizens", tags=["Citizen Management"])

@router.post("/profile", response_model=CitizenProfileRead, status_code=status.HTTP_201_CREATED)
def create_citizen_profile(profile_in: CitizenProfileCreate, db: Session = Depends(get_db)):
    profile = CitizenProfile(**profile_in.model_dump())
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

@router.get("/profile/{user_id}", response_model=CitizenProfileRead)
def get_citizen_profile(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(CitizenProfile).filter(CitizenProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Citizen profile not found")
    return profile

@router.get("/all", response_model=List[CitizenProfileRead])
def list_citizens(db: Session = Depends(get_db)):
    return db.query(CitizenProfile).all()
