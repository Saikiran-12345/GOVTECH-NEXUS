from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.org import Organization, Department, Office
from app.schemas.org import OrganizationCreate, OrganizationRead, DepartmentCreate, DepartmentRead, OfficeCreate, OfficeRead
from app.api.deps import get_current_active_user

router = APIRouter(prefix="/organizations", tags=["Organizations & Departments"])

@router.post("", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
def create_organization(org_in: OrganizationCreate, db: Session = Depends(get_db), current_user=Depends(get_current_active_user)):
    org = Organization(**org_in.model_dump())
    db.add(org)
    db.commit()
    db.refresh(org)
    return org

@router.get("", response_model=List[OrganizationRead])
def list_organizations(db: Session = Depends(get_db)):
    return db.query(Organization).all()

@router.post("/departments", response_model=DepartmentRead, status_code=status.HTTP_201_CREATED)
def create_department(dept_in: DepartmentCreate, db: Session = Depends(get_db), current_user=Depends(get_current_active_user)):
    dept = Department(**dept_in.model_dump())
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept

@router.get("/departments/all", response_model=List[DepartmentRead])
def list_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()

@router.post("/offices", response_model=OfficeRead, status_code=status.HTTP_201_CREATED)
def create_office(office_in: OfficeCreate, db: Session = Depends(get_db), current_user=Depends(get_current_active_user)):
    office = Office(**office_in.model_dump())
    db.add(office)
    db.commit()
    db.refresh(office)
    return office

@router.get("/offices/all", response_model=List[OfficeRead])
def list_offices(db: Session = Depends(get_db)):
    return db.query(Office).all()
