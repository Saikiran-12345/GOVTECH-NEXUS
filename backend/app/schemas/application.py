from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class ApplicationCreate(BaseModel):
    service_id: int
    citizen_user_id: int
    office_id: int
    form_data: Optional[Dict[str, Any]] = None

class ApplicationRead(ApplicationCreate):
    id: int
    application_number: str
    status: str
    remarks: Optional[str] = None
    submitted_at: datetime
    class Config:
        from_attributes = True
