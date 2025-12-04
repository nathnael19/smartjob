from fastapi import FastAPI
from app.database.db import create_db_and_tables
from app.routers import auth

app = FastAPI()
app.include_router(auth.router)


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


@app.get("/")
def home():
    return {"msg": "homepage"}
