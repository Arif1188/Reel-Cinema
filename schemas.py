from pydantic import BaseModel, EmailStr

    
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(UserCreate):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str
    

class MovieBase(BaseModel):
    title: str
    description: str | None = None
    year: int | None = None
    rating: int | None = None
    genre: str | None = None
    is_active: bool = True


class MovieCreate(MovieBase):
    pass



class MovieOut(MovieBase):
    id: int
    class Config:
        orm_mode = True
        
