from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.document import UploadedDocument
from app.schemas.document import DocumentCreate, DocumentRead, VerifyDocumentRequest

router = APIRouter(prefix="/documents", tags=["Document Management & Verification"])

@router.post("", response_model=DocumentRead, status_code=status.HTTP_201_CREATED)
def record_uploaded_document(doc_in: DocumentCreate, db: Session = Depends(get_db)):
    doc = UploadedDocument(**doc_in.model_dump())
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

@router.get("/application/{app_id}", response_model=List[DocumentRead])
def list_application_documents(app_id: int, db: Session = Depends(get_db)):
    return db.query(UploadedDocument).filter(UploadedDocument.application_id == app_id).all()

@router.post("/{doc_id}/verify", response_model=DocumentRead)
def verify_document(doc_id: int, req: VerifyDocumentRequest, db: Session = Depends(get_db)):
    doc = db.query(UploadedDocument).filter(UploadedDocument.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
        
    doc.verification_status = req.status
    doc.verification_notes = req.notes
    db.commit()
    db.refresh(doc)
    return doc
