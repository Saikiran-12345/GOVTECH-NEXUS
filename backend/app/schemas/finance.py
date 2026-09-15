from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentRecordCreate(BaseModel):
    application_id: int
    citizen_user_id: int
    amount: float
    payment_method: Optional[str] = "ONLINE_BANKING"

class PaymentRecordRead(PaymentRecordCreate):
    id: int
    transaction_reference: str
    status: str
    created_at: datetime
    class Config:
        from_attributes = True
