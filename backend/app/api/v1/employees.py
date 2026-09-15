from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.employee import EmployeeProfile
from app.schemas.employee import EmployeeCreate, EmployeeRead

router = APIRouter(prefix="/employees", tags=["Employee & HR Management"])

@router.post("", response_model=EmployeeRead, status_code=status.HTTP_201_CREATED)
def create_employee(emp_in: EmployeeCreate, db: Session = Depends(get_db)):
    emp = EmployeeProfile(**emp_in.model_dump())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

@router.get("/all", response_model=List[EmployeeRead])
def list_employees(db: Session = Depends(get_db)):
    return db.query(EmployeeProfile).all()
