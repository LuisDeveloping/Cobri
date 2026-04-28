from sqlalchemy.orm import Session
from fastapi import Depends

from src.core.database.session import get_db

from src.modules.charges.domain.interfaces.charge_repository import ChargeRepository
from src.modules.charges.infrastructure.database.repositories.charge_repository_impl import (
    SqlAlchemyChargeRepository,
)


def get_charge_repository(
    db: Session = Depends(get_db),
) -> ChargeRepository:
    return SqlAlchemyChargeRepository(db)