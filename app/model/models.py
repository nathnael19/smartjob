from sqlmodel import JSON, Column, Relationship, SQLModel, Field
from pydantic import EmailStr
import uuid
from typing import Optional, List
from datetime import datetime
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    employer = "employer"
    job_seeker = "job_seeker"


class JobType(str, Enum):
    full_time = "Full time"
    part_time = "Part time"
    remote = "remote"


class Status(str, Enum):
    active = "Active"
    open = "Open to offers"
    not_active = "Not Looking"


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, nullable=False)
    password: str
    role: Role


class UserCreate(UserBase):
    pass


class User(UserCreate, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    last_login: datetime = Field(default_factory=datetime.now)

    employers: Optional["Employer"] = Relationship(back_populates="user")
    job_seekers: Optional["JobSeeker"] = Relationship(back_populates="user")


class Employer(SQLModel, table=True):
    id: uuid.UUID = Field(foreign_key="user.id", ondelete="CASCADE")
    company_name: str
    company_size: int
    industry: str
    location: str
    website_url: Optional[str] = None
    contact_email: Optional[EmailStr]
    verified: bool = Field(default=False)

    user: Optional[User] = Relationship(back_populates="employers")


class JobSeeker(SQLModel, table=True):
    id: uuid.UUID = Field(foreign_key="user.id", ondelete="CASCADE")
    full_name: str
    resume_url: str
    skills: Optional[List[str]] = Field(sa_column=Column(JSON))
    experience_year: int
    education_level: str
    preferred_job_type: Optional[JobType]
    location: str
    portfolio_url: Optional[str]
    status: Status

    user: Optional["User"] = Relationship(back_populates="job_seekers")
