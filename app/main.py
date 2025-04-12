from fastapi import FastAPI
from .routers import user, task
from .database import engine
from .models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)

print("reloaded")
@app.get("/")
def root():
    return {"message": "FastAPI server is running"}
