from sqlalchemy.orm import Session
from app.models.hall import Hall
from app.schemas.hall import HallCreate, HallUpdate

def get_hall(db: Session, hall_id: int):
    return db.query(Hall).filter(Hall.id == hall_id).first()

def get_halls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Hall).offset(skip).limit(limit).all()

def create_hall(db: Session, hall_in: HallCreate):
    db_hall = Hall(**hall_in.dict())
    db.add(db_hall)
    db.commit()
    db.refresh(db_hall)
    return db_hall

def update_hall(db: Session, hall_id: int, hall_in: HallUpdate):
    db_hall = get_hall(db, hall_id)
    if not db_hall:
        return None
    for key, value in hall_in.dict(exclude_unset=True).items():
        setattr(db_hall, key, value)
    db.commit()
    db.refresh(db_hall)
    return db_hall

def delete_hall(db: Session, hall_id: int):
    db_hall = get_hall(db, hall_id)
    if db_hall:
        db.delete(db_hall)
        db.commit()
    return db_hall