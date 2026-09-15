from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.db.session import get_db
from app.models.finance import PaymentRecord
from app.schemas.finance import PaymentRecordCreate, PaymentRecordRead

router = APIRouter(prefix="/finance", tags=["Revenue & Payment Administration"])

@router.post("/payments", response_model=PaymentRecordRead, status_code=status.HTTP_201_CREATED)
def record_payment(payment_in: PaymentRecordCreate, db: Session = Depends(get_db)):
    tx_ref = f"TXN-{uuid.uuid4().hex[:10].upper()}"
    payment = PaymentRecord(transaction_reference=tx_ref, **payment_in.model_dump())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

@router.get("/payments/all", response_model=List[PaymentRecordRead])
def list_payments(db: Session = Depends(get_db)):
    return db.query(PaymentRecord).all()
