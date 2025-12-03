from sqlmodel import SQLModel, create_engine
from app.core.config import settings

engine = create_engine(settings.postgres_url, echo=True)


def create_db_and_tables():
    from app.model.models import Auth

    SQLModel.metadata.create_all(engine)
