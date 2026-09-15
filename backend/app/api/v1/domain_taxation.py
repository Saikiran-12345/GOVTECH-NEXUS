from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_taxation import CommercialTaxAssessment
from app.schemas.domain_taxation import CommercialTaxAssessmentCreate, CommercialTaxAssessmentRead

router = APIRouter(prefix="/domain/taxation", tags=["Domain — Taxation Administration"])

@router.post("", response_model=CommercialTaxAssessmentRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: CommercialTaxAssessmentCreate, db: Session = Depends(get_db)):
    item = CommercialTaxAssessment(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[CommercialTaxAssessmentRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(CommercialTaxAssessment).all()
