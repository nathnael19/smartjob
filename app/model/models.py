from sqlmodel import Relationship, SQLModel, Field
from pydantic import EmailStr
import uuid
from typing import Optional, List
from datetime import datetime
from enum import Enum


class AuthRole(str, Enum):
    admin = "admin"
    employer = "employer"
    user = "user"


class AuthCreate(SQLModel):
    full_name: str = Field(max_length=100)
    email: EmailStr = Field(unique=True)
    password: str = Field(min_length=6, max_length=32)
    role: AuthRole = Field(default=AuthRole.user)


class Auth(AuthCreate, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    users: List["User"] = Relationship(back_populates="auth")
    admins: List["Admin"] = Relationship(back_populates="auth")
    employers: List["Employer"] = Relationship(back_populates="auth")


class User(SQLModel, table=True):
    id: uuid.UUID = Field(foreign_key="auth.id", primary_key=True, ondelete="CASCADE")
    name: str

    auth: Optional["Auth"] = Relationship(back_populates="users")


class Admin(SQLModel, table=True):
    id: uuid.UUID = Field(foreign_key="auth.id", primary_key=True, ondelete="CASCADE")
    name: str

    auth: Optional["Auth"] = Relationship(back_populates="admins")


class Employer(SQLModel, table=True):
    id: uuid.UUID = Field(foreign_key="auth.id", primary_key=True, ondelete="CASCADE")
    name: str

    auth: Optional["Auth"] = Relationship(back_populates="employers")
