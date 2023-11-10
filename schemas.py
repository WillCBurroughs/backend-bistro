from typing import Optional

from pydantic import BaseModel

class Cuisine(BaseModel):
    id: int
    name: str 

class Category(BaseModel):
    id: int
    name: str 

class MenuModel(BaseModel):
    id: int
    title: str 
    description: str 
    price: float 
    spiciness: int 
    category_id: str
    cuisine_id: str

    class Config:
        orm_mode = True
        
        
