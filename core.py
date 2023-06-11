from fastapi import FastAPI
app = FastAPI()

from pathlib import Path
import environ
import os

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECRET_KEY = env('SECRET_KEY', default='SOME_SECRET_KEY')







@app.get("/")
async def root():
    return {"message": "Hello World"}