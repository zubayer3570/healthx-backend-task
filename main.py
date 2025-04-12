from fastapi import FastAPI
from app.routers import user, task
from app.database import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)

print("reloaded")
@app.get("/")
def root():
    return {"message": "FastAPI server is running"}
