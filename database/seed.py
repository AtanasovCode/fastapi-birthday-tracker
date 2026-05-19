from model.models import Base, Person, Category
from database.database import engine, SessionLocal
from datetime import date

def seed():
    
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        # Check if DB already seeded
        if db.query(Category).count() > 0:
            print("Database already seeded, skipping")
            return None
        
        # Create categories list
        categories = [
            Category(name="Family"),
            Category(name="Friends"),
            Category(name="Coworkers")
        ]
        
        # Add to database but do not commit yet
        db.add_all(categories)
        db.flush()
        
        # Create people list
        people = [
            Person(
                name="Jake Peralta",
                birth_date = date(1981, 4, 24),
                category_id = categories[1].id
            ),
            Person(
                name="Lynn Boyle",
                birth_date=date(1968, 7, 20),
                category_id=categories[0].id
            )
        ]
        
        # Commit to database
        db.add_all(people)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        raise
    finally:
        print("Finished seeding database")
        db.close()