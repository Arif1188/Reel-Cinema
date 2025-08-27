from sqlalchemy.orm import Session
from app.models.session import Session as FilmSession
from app.schemas.session import SessionCreate, SessionUpdate

def get_session(db: Session, session_id: int):
    return db.query(FilmSession).filter(FilmSession.id == session_id).first()

def get_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FilmSession).offset(skip).limit(limit).all()

def get_sessions_by_film(db: Session, film_id: int):
    return db.query(FilmSession).filter(FilmSession.film_id == film_id).all()

def create_session(db: Session, session_in: SessionCreate):
    db_session = FilmSession(**session_in.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def update_session(db: Session, session_id: int, session_in: SessionUpdate):
    db_session = get_session(db, session_id)
    if not db_session:
        return None
    for key, value in session_in.dict(exclude_unset=True).items():
        setattr(db_session, key, value)
    db.commit()
    db.refresh(db_session)
    return db_session

def delete_session(db: Session, session_id: int):
    db_session = get_session(db, session_id)
    if db_session:
        db.delete(db_session)
        db.commit()
    return db_session