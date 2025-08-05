from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models import User
from schemas import UserCreate, UserLogin, Token
from oauth2 import hash, verify, create_access_token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()



@router.post("/create_user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pw = hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created"}


@router.delete('/delete_user/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    if user:
        db.delete(user)
        db.commit()
        return f"User {user.username} Deleted Successfully"
    else:
        return "There no user left"
    
    
    
# Register
@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(data={"sub": new_user.email})
    return {"access_token": token, "token_type": "bearer"}

# Login
@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}




