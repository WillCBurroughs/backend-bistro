from typing import Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from database import Base

class MenuItem(Base):
    __tablename__ = "menuitems"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, default="Name")
    description: str = Column(String, default="description")
    price: float = Column(Float, default="price")
    spiciness: int = Column(Integer, default="spiciness")

    # Define foreign key relationships
    category_id: int = Column(Integer, ForeignKey('category.id'))
    cuisine_id: int = Column(Integer, ForeignKey('cuisine.id'))

    # Define relationships
    category = relationship("Category", back_populates="menu_items")
    cuisine = relationship("Cuisine", back_populates="menu_items")

    def __repr__(self) -> str:
        return f"MenuItem(id={self.id!r}, title={self.title!r}, description={self.description!r}, price={self.price!r}, spiciness={self.spiciness!r}, category_id={self.category_id!r}, cuisine_id={self.cuisine_id!r})"

class Category(Base):
    __tablename__ = "category"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)

    # Define back reference for relationship
    menu_items = relationship("MenuItem", back_populates="category")

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r})"


class Cuisine(Base):
    __tablename__ = "cuisine"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)

    # Define back reference for relationship
    menu_items = relationship("MenuItem", back_populates="cuisine")

    def __repr__(self) -> str:
        return f"Cuisine(id={self.id!r}, name={self.name!r})"







    