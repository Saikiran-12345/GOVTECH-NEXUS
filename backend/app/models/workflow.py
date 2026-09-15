from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    case_number = Column(String(100), unique=True, index=True, nullable=False)
    application_id = Column(Integer, ForeignKey("service_applications.id", ondelete="CASCADE"), nullable=False)
    assigned_employee_id = Column(Integer, ForeignKey("employee_profiles.id"), nullable=True)
    priority = Column(String(20), default="MEDIUM") # LOW, MEDIUM, HIGH, URGENT
    status = Column(String(50), default="OPEN") # OPEN, UNDER_REVIEW, PENDING_APPROVAL, RESOLVED, CLOSED
    sla_due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    application = relationship("ServiceApplication")
    employee = relationship("EmployeeProfile")

class ApprovalRecord(Base):
    __tablename__ = "approval_records"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False)
    approver_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    action = Column(String(50), nullable=False) # APPROVED, REJECTED, RETURNED_FOR_CORRECTION
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    case = relationship("Case")
    approver = relationship("User")
