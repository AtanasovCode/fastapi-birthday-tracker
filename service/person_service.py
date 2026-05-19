from sqlalchemy.orm import Session
from model.schema import PersonUpdate, PersonCreate
from repo import person_repo as people

def list_all(db: Session):
    return people.list_all(db)

def find_by_id(db: Session, person_id: int):
    return people.find_by_id(db, person_id)

def save(db: Session, person_create: PersonCreate):
    return people.save(db, person_create)

def update(db: Session, person_update: PersonUpdate, person_id: int):
    return people.update(db, person_update, person_id)

def delete(db: Session, person_id: int):
    return people.delete(db, person_id)