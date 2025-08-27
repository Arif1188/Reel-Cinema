from pydantic import BaseModel
from typing import Optional

class HallBase(BaseModel):
    name: str
    seats: int

class HallCreate(HallBase):
    pass

class HallUpdate(HallBase):
    pass

class HallOut(HallBase):
    id: int

    class Config:
        orm_mode = True