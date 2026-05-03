# PAYMENT QUERIES

from typing import List, Optional
import uuid

from src.modules.payments.domain.entities.payment_entity import Payment
from src.modules.payments.domain.interfaces.payment_repository import PaymentRepository


# GET PAYMENTS BY CHARGE (HISTORIAL)
def get_payments_by_charge(
    repository: PaymentRepository,
    charge_id: uuid.UUID,
    company_id: uuid.UUID,
) -> List[Payment]:

    return repository.get_by_charge_id(
        charge_id=charge_id,
        company_id=company_id,
    )


# GET PAYMENT BY ID
def get_payment_by_id(
    repository: PaymentRepository,
    payment_id: uuid.UUID,
    company_id: uuid.UUID,
) -> Optional[Payment]:

    payment = repository.get_by_id(payment_id)

    if not payment or payment.company_id != company_id:
        return None

    return payment