
from pydantic import BaseModel, EmailStr
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

# to response back


class Post(PostBase):
    id: int

    created_at: datetime

    class Config():
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

# to response back


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config():
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
