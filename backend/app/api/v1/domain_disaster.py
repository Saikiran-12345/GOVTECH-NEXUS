from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_disaster import DisasterAlert
from app.schemas.domain_disaster import DisasterAlertCreate, DisasterAlertRead

router = APIRouter(prefix="/domain/disaster", tags=["Domain — Disaster Administration"])

@router.post("", response_model=DisasterAlertRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: DisasterAlertCreate, db: Session = Depends(get_db)):
    item = DisasterAlert(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[DisasterAlertRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(DisasterAlert).all()
