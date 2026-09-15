from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentCreate(BaseModel):
    application_id: int
    document_type: str
    original_filename: str
    stored_filename: str
    file_path: str
    file_size_bytes: int
    checksum_md5: str

class DocumentRead(DocumentCreate):
    id: int
    verification_status: str
    verification_notes: Optional[str] = None
    created_at: datetime
    class Config:
        from_attributes = True

class VerifyDocumentRequest(BaseModel):
    status: str # VERIFIED or REJECTED
    notes: Optional[str] = None
