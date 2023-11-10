from sqlalchemy.orm import session, aliased, joinedload
from models import MenuItem, Category, Cuisine
from sqlalchemy import Select
from sqlalchemy.orm import Session
from schemas import MenuModel


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

