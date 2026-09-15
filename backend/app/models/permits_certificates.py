from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Permit(Base):
    __tablename__ = "permits"

    id = Column(Integer, primary_key=True, index=True)
    permit_number = Column(String(100), unique=True, index=True, nullable=False)
    application_id = Column(Integer, ForeignKey("service_applications.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    issue_date = Column(DateTime, default=datetime.utcnow)
    expiry_date = Column(DateTime, nullable=False)
    status = Column(String(50), default="ACTIVE") # ACTIVE, EXPIRED, SUSPENDED, REVOKED
    created_at = Column(DateTime, default=datetime.utcnow)

    application = relationship("ServiceApplication")

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    certificate_number = Column(String(100), unique=True, index=True, nullable=False)
    application_id = Column(Integer, ForeignKey("service_applications.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    verification_code = Column(String(64), unique=True, index=True, nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow)
    is_revoked = Column(Boolean, default=False)

    application = relationship("ServiceApplication")
