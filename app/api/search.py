from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models.film import Film
from app.schemas.film import FilmOut

router = APIRouter()

@router.get("/", response_model=list[FilmOut])
def search_films(q: str = "", genre: str = "", sort: str = "date", db: Session = Depends(get_db)):
    query = db.query(Film)
    if q:
        query = query.filter(Film.title.ilike(f"%{q}%"))
    if genre:
        query = query.filter(Film.genre == genre)
    if sort == "date":
        query = query.order_by(Film.date.desc())
    elif sort == "popularity":
        query = query.order_by(Film.rate.desc())
    return query.all()