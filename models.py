from typing import List
from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

from database import Base

class MenuItem(Base):
    __tablename__ = "menuitems"

    id : Mapped[int] = mapped_column(primary_key = True, index = True)
    name: Mapped[str] = Column(String, default="Name")
    description: Mapped[str] = Column(String, default = "description")
    price: Mapped[int] = Column(Float, default= "price")
    spiciness: Mapped[int] = Column(Integer, default = "spiciness")

    # Define foreign key relationships
    category_id = Column(Integer, ForeignKey('categories.id'))
    cuisine_id = Column(Integer, ForeignKey('cuisines.id'))

    # Define relationships
    category = relationship("Category", back_populates="menu_items")
    cuisine = relationship("Cuisine", back_populates="menu_items")

    def __repr__(self) -> str: 
        return f"MenuItem(id={self.id!r}, name={self.name!r}, description={self.description!r}, price={self.price!r}, spiciness={self.spiciness!r}, category_id={self.category_id!r}, cuisine_id={self.cuisine_id!r})"


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r})"


class Cuisine(Base):
    __tablename__ = "cuisine"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"cuisine(id={self.id!r}, name={self.name!r})"









    