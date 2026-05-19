from sqlalchemy import (
Column,
Integer,
String,
Date,
ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "category"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    people = relationship("Person", back_populates="category")
    

class Person(Base):
    __tablename__ = "person"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Date)
    category_id = Column(Integer, ForeignKey("category.id"))
    
    category = relationship("Category", back_populates="people")
    
    