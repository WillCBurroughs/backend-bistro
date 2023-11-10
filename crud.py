from sqlalchemy.orm import session, aliased, joinedload
from models import MenuItem, Category, Cuisine
from sqlalchemy import Select
from sqlalchemy.orm import Session
from schemas import MenuModel
from fastapi import APIRouter, HTTPException, status



def get_menu_items(db: Session): 
    menu_query = (
        db.query(MenuItem)
        .options(
            joinedload(MenuItem.category)  # Use joinedload on the relationship property
        )
        .all()
    )

    menu = {}
    for item in menu_query:
        mid = item.id
    # Construct Pydantic models manually
        menu_item = MenuModel(
            id=item.id,
            title=item.title,
            description=item.description,
            price=item.price,
            spiciness=item.spiciness,
            category_id = item.category.name,
            cuisine_id = item.cuisine.name
        )
        menu[mid] = menu_item

    return_menu = list(menu.values())

    return return_menu


def get_menu_item_by_id(db: Session, item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    
    if menu_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    
    # Construct Pydantic model manually
    menu_item_model = MenuModel(
        id=menu_item.id,
        title=menu_item.title,
        description=menu_item.description,
        price=menu_item.price,
        spiciness=menu_item.spiciness,
        category_id=menu_item.category.name,
        cuisine_id=menu_item.cuisine.name
    )

    return menu_item_model
    