from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.domain_transport import VehiclePermit
from app.schemas.domain_transport import VehiclePermitCreate, VehiclePermitRead

router = APIRouter(prefix="/domain/transport", tags=["Domain — Transport Administration"])

@router.post("", response_model=VehiclePermitRead, status_code=status.HTTP_201_CREATED)
def create_record(item_in: VehiclePermitCreate, db: Session = Depends(get_db)):
    item = VehiclePermit(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/all", response_model=List[VehiclePermitRead])
def list_records(db: Session = Depends(get_db)):
    return db.query(VehiclePermit).all()
