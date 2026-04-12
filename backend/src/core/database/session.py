from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.core.config import settings


# Base para modelos ORM
class Base(DeclarativeBase):
    pass


# Crear engine (Es la conexión a PostgreSQL)
engine = create_engine(
    settings.database_url,
    echo=True  # 👈 luego lo quitamos en producción
)


# Crear sesión de base de datos
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# Dependency para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()