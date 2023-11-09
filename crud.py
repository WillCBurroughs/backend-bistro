from fastapi import FastAPI
# the equivalent of this from models import Hero, Ability, AbilityType, Relationships, RelationshipType
from sqlalchemy import Select
from enum import Enum

#  from routes import (Something)

app = FastAPI()
# app.include_router(Value to include)

@app.get("/")
async def read_root():
    return {"msg": "Hello World"}
