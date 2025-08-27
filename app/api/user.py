from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db, get_current_user
from app.schemas.user import UserOut

router = APIRouter()

@router.get("/me", response_model=UserOut)
def get_profile(current_user=Depends(get_current_user)):
    return current_user

@router.post("/change-password")
def change_password(old_password: str, new_password: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    from app.core.security import verify_password, get_password_hash
    if not verify_password(old_password, current_user.hashed_password):
        raise HTTPException(status_code=403, detail="Incorrect password")
    current_user.hashed_password = get_password_hash(new_password)
    db.commit()
    return {"msg": "Password updated"}