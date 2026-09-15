from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OfficeCreate(BaseModel):
    department_id: int
    name: str
    code: str
    city: str
    state: str
    pincode: str
    address: Optional[str] = None

class OfficeRead(OfficeCreate):
    id: int
    is_active: bool
    created_at: datetime
    class Config:
        from_attributes = True

class DepartmentCreate(BaseModel):
    organization_id: int
    name: str
    code: str
    description: Optional[str] = None
    head_name: Optional[str] = None

class DepartmentRead(DepartmentCreate):
    id: int
    is_active: bool
    created_at: datetime
    offices: List[OfficeRead] = []
    class Config:
        from_attributes = True

class OrganizationCreate(BaseModel):
    name: str
    code: str
    jurisdiction: str
    address: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None

class OrganizationRead(OrganizationCreate):
    id: int
    is_active: bool
    created_at: datetime
    departments: List[DepartmentRead] = []
    class Config:
        from_attributes = True
