from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import registry

from app.core import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

mapper_registry = registry()
Base = mapper_registry.generate_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
