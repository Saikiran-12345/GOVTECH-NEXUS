from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class PaymentRecord(Base):
    __tablename__ = "payment_records"

    id = Column(Integer, primary_key=True, index=True)
    transaction_reference = Column(String(100), unique=True, index=True, nullable=False)
    application_id = Column(Integer, ForeignKey("service_applications.id", ondelete="CASCADE"), nullable=False)
    citizen_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String(50), default="ONLINE_BANKING") # ONLINE_BANKING, CARD, UPI, CHALLAN
    status = Column(String(50), default="COMPLETED") # INITIATED, VERIFIED, COMPLETED, REFUNDED
    created_at = Column(DateTime, default=datetime.utcnow)

    application = relationship("ServiceApplication")
    citizen = relationship("User")
