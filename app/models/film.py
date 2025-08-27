from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from app.models.base import Base


class Film(Base):
    __tablename__ = 'films'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    duration = Column(Integer)
    date = Column(DateTime)
    genre = Column(String)
    rate = Column(Integer)
    
    




