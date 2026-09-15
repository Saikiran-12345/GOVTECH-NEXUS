from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_education import EducationScholarship
from app.schemas.domain_education import EducationScholarshipCreate, EducationScholarshipRead

router = APIRouter(prefix="/domain/education", tags=["Domain — Education Administration"])

@router.post("", response_model=EducationScholarshipRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: EducationScholarshipCreate, db: Session = Depends(get_db)):
    item = EducationScholarship(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[EducationScholarshipRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(EducationScholarship).all()
