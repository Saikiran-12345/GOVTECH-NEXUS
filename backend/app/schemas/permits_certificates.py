from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PermitCreate(BaseModel):
    application_id: int
    title: str
    expiry_date: datetime

class PermitRead(PermitCreate):
    id: int
    permit_number: str
    issue_date: datetime
    status: str
    created_at: datetime
    class Config:
        from_attributes = True

class CertificateCreate(BaseModel):
    application_id: int
    title: str

class CertificateRead(CertificateCreate):
    id: int
    certificate_number: str
    verification_code: str
    issued_at: datetime
    is_revoked: bool
    class Config:
        from_attributes = True
