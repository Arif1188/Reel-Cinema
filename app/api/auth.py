from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_email
from app.core.security import get_password_hash, verify_password, create_access_token
from app.deps import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = get_user_by_email(db, user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = get_password_hash(user_in.password)
    user = create_user(db, user_in, hashed_pw)
    # TODO: send confirmation email here
    return user

from fastapi import Form

@router.post("/login")
def login(
    username: str = Form(...),   # OAuth2 spec requires "username"
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # If you use email as login, treat "username" as email
    user = get_user_by_email(db, username)

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )

    if not user.confirmed:
        raise HTTPException(
            status_code=403,
            detail="Email not confirmed"
        )

    access_token = create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/logout")
def logout():
    # Token-based logout is handled on frontend by deleting token
    return {"msg": "Logged out"}

@router.post("/password-reset-request")
def password_reset_request(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # TODO: send password reset email here
    return {"msg": "Password reset email sent"}

@router.post("/password-reset")
def password_reset(token: str, new_password: str, db: Session = Depends(get_db)):
    # TODO: verify token and update password
    return {"msg": "Password has been reset"}

@router.get("/confirm-email")
def confirm_email(token: str, db: Session = Depends(get_db)):
    # TODO: verify token and set user.confirmed = True
    return {"msg": "Email confirmed"}