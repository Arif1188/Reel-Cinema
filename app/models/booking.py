from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from app.models.base import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    seat_number = Column(Integer, nullable=False)
    booked_at = Column(DateTime)
    is_cancelled = Column(Boolean, default=False)
    
    
    