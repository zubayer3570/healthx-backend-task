from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.crud import crud
from app.schemas import schemas
from app import database

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task, user_id=user_id)

@router.get("/{task_id}", response_model=schemas.Task)
def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.get("/user/{user_id}", response_model=list[schemas.Task])
def read_task_by_user(user_id: int, db: Session = Depends(get_db)):
    print(user_id)
    db_task = crud.get_task_by_user(db, user_id=user_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.get("/", response_model=list[schemas.Task])
def read_all_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tasks(db=db, skip=skip, limit=limit)

