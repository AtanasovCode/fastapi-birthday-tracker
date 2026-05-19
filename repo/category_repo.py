from sqlalchemy.orm import Session
from model.models import Category

def list_all(db: Session):
    return db.query(Category).all()