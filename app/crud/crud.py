from sqlalchemy.orm import Session, joinedload
from ..models import models
from ..schemas import schemas
from typing import Optional

# User CRUD Operations

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# Task CRUD Operations

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(title=task.title, description=task.description, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_task_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).options(joinedload(models.Task.user)).all()