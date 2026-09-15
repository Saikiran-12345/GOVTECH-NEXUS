from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class CitizenProfile(Base):
    __tablename__ = "citizen_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    national_id = Column(String(100), unique=True, index=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(20), nullable=False)
    permanent_address = Column(Text, nullable=False)
    current_address = Column(Text, nullable=False)
    occupation = Column(String(100), nullable=True)
    annual_income = Column(Integer, default=0)
    category = Column(String(50), default="GENERAL") # GENERAL, OBC, SC, ST
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
