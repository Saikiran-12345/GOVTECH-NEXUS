from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_welfare import WelfareScheme
from app.schemas.domain_welfare import WelfareSchemeCreate, WelfareSchemeRead

router = APIRouter(prefix="/domain/welfare", tags=["Domain — Welfare Administration"])

@router.post("", response_model=WelfareSchemeRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: WelfareSchemeCreate, db: Session = Depends(get_db)):
    item = WelfareScheme(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[WelfareSchemeRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(WelfareScheme).all()
