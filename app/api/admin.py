from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db, get_current_admin_user
from app.crud.film import get_films
from app.crud.session import get_sessions
from app.crud.booking import get_bookings

router = APIRouter()

@router.get("/dashboard")
def admin_dashboard(db: Session = Depends(get_db), admin=Depends(get_current_admin_user)):
    films = get_films(db)
    sessions = get_sessions(db)
    bookings = get_bookings(db)
    return {
        "films": films,
        "sessions": sessions,
        "bookings": bookings
    }
    
    