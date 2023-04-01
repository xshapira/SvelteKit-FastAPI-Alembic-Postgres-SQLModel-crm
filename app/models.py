from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# from database import Base

from typing import List, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine

###############################################################################
# User
class UserBase(SQLModel):
    name: str = Field(index=True)
    email: str
    password: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    posts: List["Post"] = Relationship(back_populates="author")

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

class UserRead(UserBase):
    id: int

class UserUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

###############################################################################
# Post
class PostBase(SQLModel):
    title: str
    body: str
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")


class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author: Optional[User] = Relationship(back_populates="posts")

class PostRead(PostBase):
    id: Optional[int] = None

class PostCreate(PostBase):
    pass

class PostUpdate(SQLModel):
    id: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    author_id: Optional[int] = None

class PostReadWithUser(PostRead):
    author: Optional[UserRead] = None

class UserReadWithPosts(UserRead):
    posts: List[PostRead] = []

###############################################################################
# Auth
class Login(SQLModel):
    username: str
    password: str


class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    email: str | None = None

###############################################################################
