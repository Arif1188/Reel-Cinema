from fastapi import FastAPI
import models
from database import engine
import user, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(crud.router)
app.include_router(user.router)