from sqlalchemy.orm import Session
from app.models.film import Film
from app.schemas.film import FilmCreate, FilmUpdate

def get_film(db: Session, film_id: int):
    return db.query(Film).filter(Film.id == film_id).first()

def get_films(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Film).offset(skip).limit(limit).all()

def create_film(db: Session, film_in: FilmCreate):
    db_film = Film(**film_in.dict())
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film

def update_film(db: Session, film_id: int, film_in: FilmUpdate):
    db_film = get_film(db, film_id)
    if not db_film:
        return None
    for key, value in film_in.dict(exclude_unset=True).items():
        setattr(db_film, key, value)
    db.commit()
    db.refresh(db_film)
    return db_film

def delete_film(db: Session, film_id: int):
    db_film = get_film(db, film_id)
    if db_film:
        db.delete(db_film)
        db.commit()
    return db_film  