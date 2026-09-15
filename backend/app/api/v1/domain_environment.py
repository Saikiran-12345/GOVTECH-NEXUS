from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_environment import EnvironmentalClearance
from app.schemas.domain_environment import EnvironmentalClearanceCreate, EnvironmentalClearanceRead

router = APIRouter(prefix="/domain/environment", tags=["Domain — Environment Administration"])

@router.post("", response_model=EnvironmentalClearanceRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: EnvironmentalClearanceCreate, db: Session = Depends(get_db)):
    item = EnvironmentalClearance(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[EnvironmentalClearanceRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(EnvironmentalClearance).all()
