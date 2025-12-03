from sqlmodel import SQLModel, Field
from pydantic import EmailStr
import uuid
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
