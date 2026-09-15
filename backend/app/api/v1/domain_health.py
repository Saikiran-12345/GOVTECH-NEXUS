from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_health import PublicHealthRecord
from app.schemas.domain_health import PublicHealthRecordCreate, PublicHealthRecordRead

router = APIRouter(prefix="/domain/health", tags=["Domain — Health Administration"])

@router.post("", response_model=PublicHealthRecordRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: PublicHealthRecordCreate, db: Session = Depends(get_db)):
    item = PublicHealthRecord(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[PublicHealthRecordRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(PublicHealthRecord).all()
