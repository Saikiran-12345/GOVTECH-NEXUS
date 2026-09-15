from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class ServiceApplication(Base):
    __tablename__ = "service_applications"

    id = Column(Integer, primary_key=True, index=True)
    application_number = Column(String(100), unique=True, index=True, nullable=False)
    service_id = Column(Integer, ForeignKey("gov_services.id", ondelete="CASCADE"), nullable=False)
    citizen_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    office_id = Column(Integer, ForeignKey("offices.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(50), default="SUBMITTED") # DRAFT, SUBMITTED, UNDER_VERIFICATION, VERIFIED, UNDER_PROCESSING, APPROVAL_PENDING, APPROVED, REJECTED, COMPLETED
    form_data = Column(JSON, nullable=True)
    remarks = Column(Text, nullable=True)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    service = relationship("GovService")
    citizen = relationship("User")
    office = relationship("Office")
