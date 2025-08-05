from sqlalchemy import Column, Integer, String, Boolean
from database import Base
import enum

class UserRole(enum.Enum):
    USER = "user"
    ADMIN = "admin"


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    rating = Column(Integer, nullable=True)
    genre = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    