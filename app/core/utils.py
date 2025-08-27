from typing import Optional
from datetime import datetime

def get_current_time():
    return datetime.utcnow()

def safe_int(value: Optional[str], default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

def get_object_or_404(obj, message="Object not found"):
    if obj is None:
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
    return obj