from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.database.session import get_db
from src.modules.clients.infrastructure.database.repositories.client_repository_impl import (
    SqlAlchemyClientRepository,
)


def get_client_repository(db: Session = Depends(get_db)):
    return SqlAlchemyClientRepository(db)