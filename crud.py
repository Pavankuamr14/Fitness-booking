from sqlmodel import Session, select
from models import FitnessClass, Booking
from datetime import datetime

def get_all_classes(session: Session):
    return session.exec(select(FitnessClass)).all()

def get_class_by_id(session: Session, class_id: int):
    return session.get(FitnessClass, class_id)

def create_booking(session: Session, class_id: int, client_name: str, client_email: str):
    fit_class = get_class_by_id(session, class_id)
    if not fit_class:
        return None, "Class not found"
    if fit_class.available_slots <= 0:
        return None, "No available slots"
    fit_class.available_slots -= 1
    booking = Booking(
        class_id=class_id,
        client_name=client_name,
        client_email=client_email,
        booking_time=datetime.utcnow()
    )
    session.add(booking)
    session.add(fit_class)
    session.commit()
    session.refresh(booking)
    return booking, None

def get_bookings_by_email(session: Session, email: str):
    return session.exec(select(Booking).where(Booking.client_email == email)).all()
