from typing import Any
from sqlmodel import Session
from app.core.depencies import database_dep


def add_to_db(db: database_dep, model: Any):
    db.add(model)
    db.commit()
    db.refresh(model)

    return model
