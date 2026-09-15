from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class UploadedDocument(Base):
    __tablename__ = "uploaded_documents"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("service_applications.id", ondelete="CASCADE"), nullable=False)
    document_type = Column(String(100), nullable=False) # ID_PROOF, ADDRESS_PROOF, INCOME_CERTIFICATE
    original_filename = Column(String(255), nullable=False)
    stored_filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_size_bytes = Column(Integer, nullable=False)
    checksum_md5 = Column(String(64), nullable=False)
    verification_status = Column(String(50), default="PENDING") # PENDING, VERIFIED, REJECTED
    verification_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    application = relationship("ServiceApplication")
