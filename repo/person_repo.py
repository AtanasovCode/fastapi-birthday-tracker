from sqlalchemy.orm import Session
from model.models import Person
from model.schema import PersonCreate, PersonUpdate

# List all people
def list_all(db: Session):
    return db.query(Person).all()

# Find person by their ID
def find_by_id(db: Session, person_id: int):
    return db.query(Person).filter(Person.id == person_id).first()
    
# Create new person
def save(db: Session, person_create: PersonCreate):
    new_person = Person(**person_create.model_dump())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person


# Update existing person's data
def update(db: Session, person_update: PersonUpdate, person_id: int):
    target = find_by_id(db, person_id)
    
    if not target:
        return None
    
    for key, value in person_update.model_dump(exclude_unset=True).items():
        setattr(target, key, value)
        
    db.commit()
    db.refresh(target)
    return target


# Delete person
def delete(db: Session, person_id: int):
    target = find_by_id(db, person_id)
    
    if not target:
        return None
        
    db.delete(target)
    db.commit()
    return target