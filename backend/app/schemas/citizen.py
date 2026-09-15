from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class CitizenProfileCreate(BaseModel):
    user_id: int
    national_id: str
    date_of_birth: date
    gender: str
    permanent_address: str
    current_address: str
    occupation: Optional[str] = None
    annual_income: Optional[int] = 0
    category: Optional[str] = "GENERAL"

class CitizenProfileRead(CitizenProfileCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
