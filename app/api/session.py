from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db, get_current_admin_user
from app.schemas.session import SessionCreate, SessionUpdate, SessionOut
from app.crud.session import get_session, get_sessions, create_session, update_session, delete_session, get_sessions_by_film

router = APIRouter()

@router.get("/", response_model=list[SessionOut])
def all_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_sessions(db, skip, limit)

@router.get("/{session_id}", response_model=SessionOut)
def session_detail(session_id: int, db: Session = Depends(get_db)):
    session = get_session(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.get("/film/{film_id}", response_model=list[SessionOut])
def sessions_by_film(film_id: int, db: Session = Depends(get_db)):
    return get_sessions_by_film(db, film_id)

@router.post("/", response_model=SessionOut)
def add_session(session_in: SessionCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin_user)):
    return create_session(db, session_in)

@router.put("/{session_id}", response_model=SessionOut)
def edit_session(session_id: int, session_in: SessionUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin_user)):
    session = update_session(db, session_id, session_in)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.delete("/{session_id}")
def remove_session(session_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin_user)):
    session = delete_session(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"msg": "Session deleted"}