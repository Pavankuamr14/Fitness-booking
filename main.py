from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List
from sqlmodel import Session, select
from database import create_db_and_tables, get_session
from models import FitnessClass, Booking
from crud import get_all_classes, create_booking, get_bookings_by_email
from pydantic import BaseModel, EmailStr
from datetime import datetime
from utils import ist_to_timezone
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Fitness Booking API")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/index.html") as f:
        return f.read()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    # Seed initial data
    with next(get_session()) as session:
        if not session.exec(select(FitnessClass)).all():
            classes = [
                FitnessClass(name="Yoga", datetime_ist=datetime(2025, 6, 16, 7, 0), instructor="Anita", total_slots=10, available_slots=10),
                FitnessClass(name="Zumba", datetime_ist=datetime(2025, 6, 16, 18, 0), instructor="Ravi", total_slots=15, available_slots=15),
                FitnessClass(name="HIIT", datetime_ist=datetime(2025, 6, 17, 6, 30), instructor="Maya", total_slots=12, available_slots=12)
            ]
            session.add_all(classes)
            session.commit()

@app.get("/classes", response_model=List[FitnessClass])
def list_classes(timezone: str = "UTC", session: Session = Depends(get_session)):
    classes = get_all_classes(session)
    for cls in classes:
        cls.datetime_ist = ist_to_timezone(cls.datetime_ist, to_tz=timezone)
    return classes

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

@app.post("/book", response_model=Booking)
def book_class(request: BookingRequest, session: Session = Depends(get_session)):
    booking, error = create_booking(session, request.class_id, request.client_name, request.client_email)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return booking

@app.get("/bookings", response_model=List[Booking])
def get_bookings(email: EmailStr = Query(...), session: Session = Depends(get_session)):
    return get_bookings_by_email(session, email)
