from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_procurement import PublicTender
from app.schemas.domain_procurement import PublicTenderCreate, PublicTenderRead

router = APIRouter(prefix="/domain/procurement", tags=["Domain — Procurement Administration"])

@router.post("", response_model=PublicTenderRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: PublicTenderCreate, db: Session = Depends(get_db)):
    item = PublicTender(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[PublicTenderRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(PublicTender).all()
