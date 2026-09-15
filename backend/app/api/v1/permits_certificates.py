from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.db.session import get_db
from app.models.permits_certificates import Permit, Certificate
from app.schemas.permits_certificates import PermitCreate, PermitRead, CertificateCreate, CertificateRead

router = APIRouter(prefix="/permits-certificates", tags=["Permit & Certificate Management"])

@router.post("/permits", response_model=PermitRead, status_code=status.HTTP_201_CREATED)
def issue_permit(permit_in: PermitCreate, db: Session = Depends(get_db)):
    p_num = f"PRM-{uuid.uuid4().hex[:8].upper()}"
    permit = Permit(permit_number=p_num, **permit_in.model_dump())
    db.add(permit)
    db.commit()
    db.refresh(permit)
    return permit

@router.get("/permits/all", response_model=List[PermitRead])
def list_permits(db: Session = Depends(get_db)):
    return db.query(Permit).all()

@router.post("/certificates", response_model=CertificateRead, status_code=status.HTTP_201_CREATED)
def generate_certificate(cert_in: CertificateCreate, db: Session = Depends(get_db)):
    c_num = f"CRT-{uuid.uuid4().hex[:8].upper()}"
    v_code = f"VERIFY-{uuid.uuid4().hex[:12].upper()}"
    cert = Certificate(certificate_number=c_num, verification_code=v_code, **cert_in.model_dump())
    db.add(cert)
    db.commit()
    db.refresh(cert)
    return cert

@router.get("/certificates/verify/{v_code}", response_model=CertificateRead)
def verify_certificate(v_code: str, db: Session = Depends(get_db)):
    cert = db.query(Certificate).filter(Certificate.verification_code == v_code).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Invalid verification code")
    return cert
