from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookingBase(BaseModel):
    user_id: int
    session_id: int
    seat_number: int

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    is_cancelled: Optional[bool] = None

class BookingOut(BookingBase):
    id: int
    booked_at: Optional[datetime]
    is_cancelled: bool

    class Config:
        orm_mode = True