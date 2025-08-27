from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db, get_current_user
from app.schemas.booking import BookingCreate, BookingUpdate, BookingOut
from app.crud.booking import get_booking, get_bookings_by_user, create_booking, update_booking, delete_booking

router = APIRouter()

@router.get("/", response_model=list[BookingOut])
def my_bookings(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_bookings_by_user(db, current_user.id)

@router.post("/", response_model=BookingOut)
def book_seat(booking_in: BookingCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Add seat availability validation here if needed
    booking_in.user_id = current_user.id  # Ensure user can't book for another user
    return create_booking(db, booking_in)

@router.put("/{booking_id}", response_model=BookingOut)
def cancel_booking(booking_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    booking = get_booking(db, booking_id)
    if not booking or booking.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Booking not found")
    booking = update_booking(db, booking_id, BookingUpdate(is_cancelled=True))
    return booking

@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    booking = get_booking(db, booking_id)
    if not booking or booking.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Booking not found")
    delete_booking(db, booking_id)
    return {"msg": "Booking deleted"}