from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.core.depencies import get_session
from app.model.models import Auth, AuthCreate, User, Admin, Employer
from app.utils.helpers import add_to_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/", response_model=Auth)
def sign_up(user: AuthCreate, db: Session = Depends(get_session)):
    user_db = Auth.model_validate(user)
    try:
        if user_db.role == "user":
            add_to_db(db, user_db)
            usr = User(id=user_db.id, name=user_db.full_name)
            add_to_db(db, usr)
        elif user_db.role == "admin":
            add_to_db(db, user_db)
            usr = Admin(id=user_db.id, name=user_db.full_name)
            add_to_db(db, usr)
        else:
            add_to_db(db, user_db)
            usr = Employer(id=user_db.id, name=user_db.full_name)
            add_to_db(db, usr)

    except:
        raise HTTPException(
            detail="email already exists", status_code=status.HTTP_409_CONFLICT
        )

    return user_db
