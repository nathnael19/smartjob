from typing import Annotated
from app.database.db import engine
from sqlmodel import Session


def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()


database_dep = Annotated[Session, get_session]
