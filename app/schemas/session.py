from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SessionBase(BaseModel):
    film_id: int
    hall_id: int
    start_time: datetime
    end_time: datetime

class SessionCreate(SessionBase):
    pass

class SessionUpdate(SessionBase):
    pass

class SessionOut(SessionBase):
    id: int

    class Config:
        orm_mode = True