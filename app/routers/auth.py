from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.core.depencies import get_session
from app.utils.helpers import add_to_db
from app.services.supabase import supabase

router = APIRouter(prefix="/auth", tags=["Authentication"])
