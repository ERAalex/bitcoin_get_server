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
from sqlalchemy import desc
import databases
from models import deribit_coins_model


# PostgreSQL - settings
DB_USER = env("DB_USER", default="user")
DB_PASSWORD = env("DB_PASSWORD", default="password")
DB_HOST = env("DB_HOST", default="localhost")
DB_NAME = env("DB_NAME", default="db_name")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

async_url = env("async_url", default="async_url")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


database = databases.Database(SQLALCHEMY_DATABASE_URL)


@app.get("/coin/{coin}")
async def read_notes(coin):
    """ Get all data about coin by it's name - btc or eth """

    query = deribit_coins_model.select().where(deribit_coins_model.c.coin_name == coin)
    return await database.fetch_all(query)


@app.get("/coin_last/{coin}")
async def read_notes(coin):
    """ Get last data about some coin - btc or eth """

    query = deribit_coins_model.select().where(
        deribit_coins_model.c.coin_name == coin).\
        order_by(desc(deribit_coins_model.c.created_at)).limit(1)
    return await database.fetch_all(query)


@app.get("/coin/{unix_time}/{coin}")
async def read_notes(unix_time, coin):
    """ Get some coin by UNIX time """

    query = deribit_coins_model.select().where(
        deribit_coins_model.c.coin_name == coin,
        deribit_coins_model.c.created_at == unix_time)
    return await database.fetch_all(query)


@app.get("/")
async def root():
    return {"message": "Hello World"}
