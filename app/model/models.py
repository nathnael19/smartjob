from sqlmodel import Relationship, SQLModel, Field
from pydantic import EmailStr
import uuid
from typing import Optional, List
from datetime import datetime
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    employer = "employer"
    user = "user"


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, nullable=False)
    password: str
    role: Role


class UserCreate(UserBase):
    pass


class User(UserCreate, table=True):
    __tablename__ = "users"  # type: ignore
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    last_login: datetime = Field(default_factory=datetime.now)
