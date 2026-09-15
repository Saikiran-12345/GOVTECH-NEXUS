from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from datetime import datetime
from app.db.database import Base

class PublicTender(Base):
    __tablename__ = "public_tenders"

    id = Column(Integer, primary_key=True, index=True)
    reference_code = Column(String(100), unique=True, index=True, nullable=False)
    title = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    amount = Column(Float, default=0.0)
    status = Column(String(50), default="ACTIVE")
    remarks = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
