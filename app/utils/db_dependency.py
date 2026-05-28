from app.database import SessionLocal

# Database session dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()