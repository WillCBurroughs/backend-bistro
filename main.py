from fastapi import FastAPI
from models import MenuItem, Cuisine, Category
from sqlalchemy import select
from enum import Enum

from routes import menu

app = FastAPI()
app.include_router(menu.router)

@app.get("/")
async def read_root():
    return {"msg": "Hello World"}
