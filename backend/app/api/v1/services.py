from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.service_catalog import GovService
from app.schemas.service_catalog import GovServiceCreate, GovServiceRead

router = APIRouter(prefix="/services", tags=["Government Service Catalog"])

@router.post("", response_model=GovServiceRead, status_code=status.HTTP_201_CREATED)
def create_service(service_in: GovServiceCreate, db: Session = Depends(get_db)):
    service = GovService(**service_in.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

@router.get("/all", response_model=List[GovServiceRead])
def list_services(db: Session = Depends(get_db)):
    return db.query(GovService).all()
