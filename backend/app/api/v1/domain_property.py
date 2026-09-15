from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_property import LandPropertyRecord
from app.schemas.domain_property import LandPropertyRecordCreate, LandPropertyRecordRead

router = APIRouter(prefix="/domain/property", tags=["Domain — Property Administration"])

@router.post("", response_model=LandPropertyRecordRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: LandPropertyRecordCreate, db: Session = Depends(get_db)):
    item = LandPropertyRecord(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[LandPropertyRecordRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(LandPropertyRecord).all()
