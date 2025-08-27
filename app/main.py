from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.auth import router as auth_router
from app.api.admin import router as admin_router
from app.api.booking import router as booking_router
from app.api.user import router as user_router
from app.api.search import router as search_router
from app.api.session import router as session_router
from app.api.film import router as film_router
from app.models.base import Base  # or the shared Base if you defined one
from app.deps import engine 
from app.config import settings

from app.models.user import User
from app.models.film import Film
from app.models.session import Session
from app.models.booking import Booking
from app.models.hall import Hall

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files and templates setup
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(film_router, prefix="/films", tags=["films"])
app.include_router(session_router, prefix="/sessions", tags=["sessions"])
app.include_router(booking_router, prefix="/bookings", tags=["bookings"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])

# Root endpoint
@app.get("/", tags=["root"])
def read_root():
    return {"msg": "Welcome to the Online Cinema!"}