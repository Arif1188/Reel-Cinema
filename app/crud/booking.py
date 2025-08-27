from sqlalchemy.orm import Session
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingUpdate

def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()

def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Booking).offset(skip).limit(limit).all()

def get_bookings_by_user(db: Session, user_id: int):
    return db.query(Booking).filter(Booking.user_id == user_id).all()

def get_bookings_by_session(db: Session, session_id: int):
    return db.query(Booking).filter(Booking.session_id == session_id).all()

def create_booking(db: Session, booking_in: BookingCreate):
    db_booking = Booking(**booking_in.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def update_booking(db: Session, booking_id: int, booking_in: BookingUpdate):
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        return None
    for key, value in booking_in.dict(exclude_unset=True).items():
        setattr(db_booking, key, value)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def delete_booking(db: Session, booking_id: int):
    db_booking = get_booking(db, booking_id)
    if db_booking:
        db.delete(db_booking)
        db.commit()
    return db_booking