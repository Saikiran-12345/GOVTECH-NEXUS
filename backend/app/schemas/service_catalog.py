from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GovServiceCreate(BaseModel):
    department_id: int
    service_code: str
    name: str
    description: Optional[str] = None
    category: str
    fee: Optional[float] = 0.0
    sla_days: Optional[int] = 7
    requires_inspection: Optional[bool] = False

class GovServiceRead(GovServiceCreate):
    id: int
    is_active: bool
    created_at: datetime
    class Config:
        from_attributes = True
