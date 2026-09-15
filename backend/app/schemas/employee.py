from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class EmployeeCreate(BaseModel):
    user_id: int
    department_id: int
    office_id: int
    employee_code: str
    designation: str
    joining_date: date

class EmployeeRead(EmployeeCreate):
    id: int
    status: str
    created_at: datetime
    class Config:
        from_attributes = True
