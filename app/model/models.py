from sqlmodel import SQLModel, Field
from pydantic import EmailStr
import uuid
from datetime import datetime
from enum import Enum


class AuthRole(str, Enum):
    admin = "admin"
    employer = "employer"
    user = "user"


class AuthBase(SQLModel):
    id: uuid.UUID = Field(primary_key=True, default=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class Auth(AuthBase, table=True):
    email: EmailStr = Field(unique=True)
    password: str = Field(min_length=6, max_length=32)
    role: AuthRole = Field(default=AuthRole.user)
