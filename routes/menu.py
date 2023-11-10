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
    # Create a crud operation to return the list of heroes 
    # db.query(models.user)
    item = crud.get_menu_items(db)
    return item