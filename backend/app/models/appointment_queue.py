from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    citizen_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    office_id = Column(Integer, ForeignKey("offices.id", ondelete="CASCADE"), nullable=False)
    service_id = Column(Integer, ForeignKey("gov_services.id"), nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(String(50), default="SCHEDULED") # SCHEDULED, COMPLETED, CANCELLED, NO_SHOW
    purpose = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    citizen = relationship("User")
    office = relationship("Office")
    service = relationship("GovService")

class QueueTicket(Base):
    __tablename__ = "queue_tickets"

    id = Column(Integer, primary_key=True, index=True)
    ticket_number = Column(String(50), unique=True, index=True, nullable=False)
    office_id = Column(Integer, ForeignKey("offices.id", ondelete="CASCADE"), nullable=False)
    citizen_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("gov_services.id"), nullable=False)
    counter_number = Column(String(20), nullable=True)
    status = Column(String(50), default="WAITING") # WAITING, CALLING, IN_SERVICE, COMPLETED, SKIPPED
    wait_time_minutes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    office = relationship("Office")
    citizen = relationship("User")
    service = relationship("GovService")
