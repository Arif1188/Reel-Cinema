from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FilmBase(BaseModel):
    title: str
    description: Optional[str] = None
    duration: Optional[int] = None
    date: Optional[datetime] = None
    genre: Optional[str] = None
    rate: Optional[float] = None

class FilmCreate(FilmBase):
    pass

class FilmUpdate(FilmBase):
    pass

class FilmOut(FilmBase):
    id: int

    class Config:
        orm_mode = True