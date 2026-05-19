from sqlalchemy.orm import Session
from repo import category_repo as categories

def list_all(db: Session):
    return categories.list_all(db)