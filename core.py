from fastapi import FastAPI
app = FastAPI()

from pathlib import Path
import environ
import os

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# (modules for async work with DB)
import asyncpg
import databases


# PostgreSQL - settings

DB_USER = env("DB_USER", default="user")
DB_PASSWORD = env("DB_PASSWORD", default="password")
DB_HOST = env("DB_HOST", default="localhost")
DB_NAME = env("DB_NAME", default="db_name")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)





@app.get("/")
async def root():
    return {"message": "Hello World"}