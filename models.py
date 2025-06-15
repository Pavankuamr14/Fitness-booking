from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class FitnessClass(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    datetime_ist: datetime
    instructor: str
    total_slots: int
    available_slots: int

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    class_id: int
    client_name: str
    client_email: str
    booking_time: datetime
