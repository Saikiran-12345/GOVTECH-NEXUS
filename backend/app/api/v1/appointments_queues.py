from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.db.session import get_db
from app.models.appointment_queue import Appointment, QueueTicket
from app.schemas.appointment_queue import AppointmentCreate, AppointmentRead, QueueTicketCreate, QueueTicketRead

router = APIRouter(prefix="/queues-appointments", tags=["Queue & Appointment Management"])

@router.post("/appointments", response_model=AppointmentRead, status_code=status.HTTP_201_CREATED)
def book_appointment(apt_in: AppointmentCreate, db: Session = Depends(get_db)):
    apt = Appointment(**apt_in.model_dump())
    db.add(apt)
    db.commit()
    db.refresh(apt)
    return apt

@router.get("/appointments/all", response_model=List[AppointmentRead])
def list_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()

@router.post("/tickets", response_model=QueueTicketRead, status_code=status.HTTP_201_CREATED)
def generate_queue_ticket(ticket_in: QueueTicketCreate, db: Session = Depends(get_db)):
    t_num = f"Q-{uuid.uuid4().hex[:6].upper()}"
    ticket = QueueTicket(ticket_number=t_num, **ticket_in.model_dump())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

@router.get("/tickets/office/{office_id}", response_model=List[QueueTicketRead])
def get_office_queue(office_id: int, db: Session = Depends(get_db)):
    return db.query(QueueTicket).filter(QueueTicket.office_id == office_id).all()
