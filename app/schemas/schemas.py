from pydantic import BaseModel
from typing import Optional

# User Schema

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int  # This field will represent the user's ID in the response

    model_config = {
        "from_attributes": True
    }

# Task Schema

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    user_id: int  # Foreign key to User
    user: User

    model_config = {
        "from_attributes": True
    }
