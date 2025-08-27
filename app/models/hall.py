from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Hall(Base):
    __tablename__ = "halls"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    seats = Column(Integer, nullable=False)  # Total seats