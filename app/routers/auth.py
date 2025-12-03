from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.core.depencies import get_session
from app.model.models import Auth, AuthCreate
from app.utils.helpers import add_to_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/", response_model=Auth)
def sign_up(user: AuthCreate, db: Session = Depends(get_session)):
    user_db = Auth.model_validate(user)
    try:
        add_to_db(db, user_db)
    except:
        raise HTTPException(
            detail="email already exists", status_code=status.HTTP_409_CONFLICT
        )

    return user_db
