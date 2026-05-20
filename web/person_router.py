from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db
from model.schema import PersonSchema, PersonCreate, PersonUpdate
from service import person_service as people, category_service as categories


router = APIRouter(prefix="/birthdays", tags=["People"])

@router.get("/all", response_model=list[PersonSchema])
async def list_all(db: Session = Depends(get_db)):
    return people.list_all(db)


@router.get("/id/{person_id}", response_model=PersonSchema)
async def find_by_id(person_id: int, db: Session = Depends(get_db)):
    return people.find_by_id(db, person_id)


@router.post("/", response_model=PersonSchema)
async def save(person_create: PersonCreate, db: Session = Depends(get_db)):
    return people.save(db, person_create)


@router.put("/", response_model=PersonSchema)
async def update(person_update: PersonUpdate, person_id: int, db: Session = Depends(get_db)):
    target = people.find_by_id(db, person_id)
    
    if target is not None:
        return people.update(db, person_update, person_id)
    
    return JSONResponse(status_code=404, content={"message": "Person not found"})


@router.delete("/", response_model=PersonSchema)
async def delete(person_id: int, db: Session = Depends(get_db)):
    target = people.find_by_id(db, person_id)
    
    if target is not None:
        return people.delete(db, person_id)
    
    return JSONResponse(status_code=404, content={"message": "Person not found"})