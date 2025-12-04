# app/core/security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from typing import Optional
from app.core.config import settings

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

JWT_SECRET = settings.SUPABASE_JWT_KEY
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days (adjust)


def hash_password(password: str) -> str:
    return PWD_CONTEXT.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return PWD_CONTEXT.verify(plain, hashed)


def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
