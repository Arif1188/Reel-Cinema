from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from schemas import MovieBase, MovieCreate 
from sqlalchemy.orm import Session
from oauth2 import get_current_user
from models import User


router = APIRouter()


@router.get("/movies")
def get_movies(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    movies = db.query(MovieBase).filter(MovieBase.owner_id == current_user.id).all()
    return {"movies": movies}     


@router.post("/create_movie")
def create_movie(movie: MovieCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_movie = MovieBase(title=movie.title, description=movie.description, owner_id=current_user.id)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return {"message": "Movie created successfully", "movie": new_movie}    
  

@router.put("/update_movie/{id}")
def update_movie(id: int, movie: MovieCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    existing_movie = db.query(MovieBase).filter(MovieBase.id == id, MovieBase.owner_id == current_user.id).first()
    if not existing_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    existing_movie.title = movie.title
    existing_movie.description = movie.description
    db.commit()
    db.refresh(existing_movie)
    
    return {"message": "Movie updated successfully", "movie": existing_movie}



@router.delete("/delete_movie/{id}")
def delete_movie(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    movie = db.query(MovieBase).filter(MovieBase.id == id, MovieBase.owner_id == current_user.id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    db.delete(movie)
    db.commit()
    return {"message": f"Movie {movie.title} deleted successfully"}