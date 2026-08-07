from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine=create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} #SQLite restricts connection to the thread that is created. 
)

SessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

