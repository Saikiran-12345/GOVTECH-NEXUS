from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LaborAuditRecordCreate(BaseModel):
    reference_code: str
    title: str
    category: str
    amount: Optional[float] = 0.0
    remarks: Optional[str] = None

class LaborAuditRecordRead(LaborAuditRecordCreate):
    id: int
    status: str
    created_at: datetime
    class Config:
        from_attributes = True
