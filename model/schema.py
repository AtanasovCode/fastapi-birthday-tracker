from pydantic import BaseModel
from datetime import date
from typing import Optional


class CategorySchema(BaseModel):
    id: int
    name: str


class PersonSchema(BaseModel):
    id: int
    name: str
    birth_date: date
    age: int
    category: CategorySchema
    
class PersonCreate(BaseModel):
    name: str
    birth_date: date
    category_id: int
    
    
class PersonUpdate(BaseModel):
    name: Optional[str] = None
    birth_date: Optional[date] = None
    category_id: Optional[int] = None
