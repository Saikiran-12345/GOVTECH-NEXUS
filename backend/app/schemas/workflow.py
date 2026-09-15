from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CaseCreate(BaseModel):
    application_id: int
    assigned_employee_id: Optional[int] = None
    priority: Optional[str] = "MEDIUM"

class CaseRead(CaseCreate):
    id: int
    case_number: str
    status: str
    created_at: datetime
    class Config:
        from_attributes = True

class ApprovalCreate(BaseModel):
    case_id: int
    approver_user_id: int
    action: str
    comments: Optional[str] = None

class ApprovalRead(ApprovalCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
