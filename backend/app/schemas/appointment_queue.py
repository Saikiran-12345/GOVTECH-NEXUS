from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AppointmentCreate(BaseModel):
    citizen_user_id: int
    office_id: int
    service_id: int
    scheduled_time: datetime
    purpose: Optional[str] = None

class AppointmentRead(AppointmentCreate):
    id: int
    status: str
    created_at: datetime
    class Config:
        from_attributes = True

class QueueTicketCreate(BaseModel):
    office_id: int
    citizen_user_id: int
    service_id: int

class QueueTicketRead(QueueTicketCreate):
    id: int
    ticket_number: str
    counter_number: Optional[str] = None
    status: str
    wait_time_minutes: int
    created_at: datetime
    class Config:
        from_attributes = True
