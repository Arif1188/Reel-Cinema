from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db, get_current_admin_user
from app.schemas.film import FilmCreate, FilmUpdate, FilmOut
from app.crud.film import get_film, get_films, create_film, update_film, delete_film

router = APIRouter()

@router.get("/", response_model=list[FilmOut])
def all_films(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_films(db, skip, limit)

@router.get("/{film_id}", response_model=FilmOut)
def film_detail(film_id: int, db: Session = Depends(get_db)):
    film = get_film(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

@router.post("/", response_model=FilmOut)
def add_film(film_in: FilmCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin_user)):
    return create_film(db, film_in)

@router.put("/{film_id}", response_model=FilmOut)
def edit_film(film_id: int, film_in: FilmUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin_user)):
    film = update_film(db, film_id, film_in)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

@router.delete("/{film_id}")
def remove_film(film_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin_user)):
    film = delete_film(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return {"msg": "Film deleted"}


