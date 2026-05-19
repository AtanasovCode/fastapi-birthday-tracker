from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from database.database import get_db
from model.schema import PersonSchema
from service import person_service as people, category_service as categories


router = APIRouter(prefix="/birthdays", tags=["People"])

@router.get("/", response_model=list[PersonSchema])
def list_all(db: Session = Depends(get_db)):
    return people.list_all(db)