from sqlalchemy.orm import Session
from fastapi import Depends

from src.core.database.session import get_db

from src.modules.payments.domain.interfaces.payment_repository import PaymentRepository
from src.modules.payments.infrastructure.database.repositories.payment_repository_impl import (
    SqlAlchemyPaymentRepository,
)


def get_payment_repository(
    db: Session = Depends(get_db),
) -> PaymentRepository:
    return SqlAlchemyPaymentRepository(db)