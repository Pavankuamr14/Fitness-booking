from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List
from sqlmodel import Session, select
from database import create_db_and_tables, get_session
from models import FitnessClass, Booking
from crud import get_all_classes, create_booking, get_bookings_by_email
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta, time
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pytz import timezone as pytz_timezone
import pytz

app = FastAPI(title="Fitness Booking API")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/index.html") as f:
        return f.read()

# --- Utility: Generate datetime based on UTC hour ---
def generate_class_datetime(hour_utc: int, day_offset: int = 0):
    today = datetime.utcnow().date() + timedelta(days=day_offset)
    return datetime.combine(today, time(hour_utc, 0))

# --- Utility: Convert from IST to target timezone ---
def ist_to_timezone(dt_ist, to_tz: str = "UTC"):
    ist = pytz_timezone("Asia/Kolkata")
    target = pytz_timezone(to_tz)
    dt_localized = ist.localize(dt_ist) if dt_ist.tzinfo is None else dt_ist.astimezone(ist)
    return dt_localized.astimezone(target)

# --- Seed database on startup ---
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    with next(get_session()) as session:
        if not session.exec(select(FitnessClass)).all():
            classes = [
                FitnessClass(
                    name="Yoga", 
                    datetime_ist=generate_class_datetime(1),  # UTC+1 => IST 6:30 AM
                    instructor="Anita", 
                    total_slots=10, 
                    available_slots=10
                ),
                FitnessClass(
                    name="Zumba", 
                    datetime_ist=generate_class_datetime(2),  # UTC+2 => IST 7:30 AM
                    instructor="Ravi", 
                    total_slots=15, 
                    available_slots=15
                ),
                FitnessClass(
                    name="HIIT", 
                    datetime_ist=generate_class_datetime(0, day_offset=1),  # Next day UTC+0 => IST 5:30 AM
                    instructor="Maya", 
                    total_slots=12, 
                    available_slots=12
                ),
            ]
            session.add_all(classes)
            session.commit()

# --- API to fetch classes in any timezone ---
@app.get("/classes", response_model=List[FitnessClass])
def list_classes(timezone: str = "UTC", session: Session = Depends(get_session)):
    classes = get_all_classes(session)
    for cls in classes:
        cls.datetime_ist = ist_to_timezone(cls.datetime_ist, to_tz=timezone)
    return classes

# --- Booking Request Model ---
class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

# --- Book a class ---
@app.post("/book", response_model=Booking)
def book_class(request: BookingRequest, session: Session = Depends(get_session)):
    booking, error = create_booking(session, request.class_id, request.client_name, request.client_email)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return booking

# --- Fetch bookings by email ---
@app.get("/bookings", response_model=List[Booking])
def get_bookings(email: EmailStr = Query(...), session: Session = Depends(get_session)):
    return get_bookings_by_email(session, email)
