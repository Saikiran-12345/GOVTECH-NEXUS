from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.db.session import get_db
from app.models.workflow import Case, ApprovalRecord
from app.schemas.workflow import CaseCreate, CaseRead, ApprovalCreate, ApprovalRead

router = APIRouter(prefix="/workflows", tags=["Case & Workflow Management"])

@router.post("/cases", response_model=CaseRead, status_code=status.HTTP_201_CREATED)
def create_case(case_in: CaseCreate, db: Session = Depends(get_db)):
    case_num = f"CASE-{uuid.uuid4().hex[:8].upper()}"
    case_obj = Case(case_number=case_num, **case_in.model_dump())
    db.add(case_obj)
    db.commit()
    db.refresh(case_obj)
    return case_obj

@router.get("/cases/all", response_model=List[CaseRead])
def list_cases(db: Session = Depends(get_db)):
    return db.query(Case).all()

@router.post("/approvals", response_model=ApprovalRead, status_code=status.HTTP_201_CREATED)
def process_approval(approval_in: ApprovalCreate, db: Session = Depends(get_db)):
    case = db.query(Case).filter(Case.id == approval_in.case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
        
    approval = ApprovalRecord(**approval_in.model_dump())
    if approval_in.action == "APPROVED":
        case.status = "RESOLVED"
    elif approval_in.action == "REJECTED":
        case.status = "CLOSED"
        
    db.add(approval)
    db.commit()
    db.refresh(approval)
    return approval
