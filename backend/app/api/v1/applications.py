from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.db.session import get_db
from app.models.application import ServiceApplication
from app.schemas.application import ApplicationCreate, ApplicationRead

router = APIRouter(prefix="/applications", tags=["Service Applications"])

@router.post("", response_model=ApplicationRead, status_code=status.HTTP_201_CREATED)
def submit_application(app_in: ApplicationCreate, db: Session = Depends(get_db)):
    app_num = f"APP-{uuid.uuid4().hex[:8].upper()}"
    app_obj = ServiceApplication(
        application_number=app_num,
        **app_in.model_dump()
    )
    db.add(app_obj)
    db.commit()
    db.refresh(app_obj)
    return app_obj

@router.get("/all", response_model=List[ApplicationRead])
def list_applications(db: Session = Depends(get_db)):
    return db.query(ServiceApplication).all()

@router.get("/{app_id}", response_model=ApplicationRead)
def get_application(app_id: int, db: Session = Depends(get_db)):
    app_obj = db.query(ServiceApplication).filter(ServiceApplication.id == app_id).first()
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_obj
