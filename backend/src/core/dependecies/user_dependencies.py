from sqlalchemy.orm import Session
from fastapi import Depends

from src.core.database.session import get_db
from src.modules.users.infrastructure.database.repositories.user_repository_impl import (
    SqlAlchemyUserRepository,
)


def get_user_repository(db: Session = Depends(get_db)):
    return SqlAlchemyUserRepository(db)