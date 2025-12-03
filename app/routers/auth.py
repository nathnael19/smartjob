from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.depencies import get_session
from app.model.models import Auth, AuthCreate

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/", response_model=Auth)
def sign_up(user: AuthCreate, db: Session = Depends(get_session)):
    user_db = Auth.model_validate(user)
    print(user_db)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db
