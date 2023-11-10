from typing import List 
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database import SessionLocal
import schemas
import crud

router = APIRouter(
    prefix="/menuitem"
)

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/all", response_model=List[schemas.MenuModel])
def get_menu(db: Session = Depends(get_db)): 
    menu_items = crud.get_menu_items(db)
    return menu_items

@router.get("/{item_id}", response_model=schemas.MenuModel)
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    menu_item = crud.get_menu_item_by_id(db, item_id)
    return menu_item