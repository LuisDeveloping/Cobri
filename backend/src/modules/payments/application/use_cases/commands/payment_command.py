from datetime import datetime
import uuid

from src.modules.payments.domain.entities.payment_entity import Payment
from src.modules.payments.domain.interfaces.payment_repository import PaymentRepository
from src.modules.charges.domain.interfaces.charge_repository import ChargeRepository

def create_payment(
    repository: PaymentRepository,
    charge_repository: ChargeRepository,
    charge_id: uuid.UUID,
    amount: float,
    payment_method: str,
    paid_at: datetime,
    company_id: uuid.UUID,
    reference: str = None,
):
    # validar charge (multi-tenant)
    charge = charge_repository.get_by_id(charge_id, company_id)

    if not charge:
        raise ValueError("Cobro no encontrado")

    if charge.status == "cancelled":
        raise ValueError("No se puede pagar un cobro cancelado")

    # calcular total actual
    total_paid = repository.get_total_paid_by_charge(
        charge_id=charge_id,
        company_id=company_id,
    )

    # evitar sobrepago
    if total_paid + amount > charge.amount:
        raise ValueError("El pago excede el monto del cobro")

    # crear entidad
    payment = Payment(
        charge_id=charge_id,
        company_id=company_id,
        amount=amount,
        payment_method=payment_method,
        reference=reference,
        paid_at=paid_at,
    )

    # guardar pago
    saved_payment = repository.create(payment)

    # recalcular total actualizado
    new_total = total_paid + amount

    # actualizar estado del charge (DOMINIO)
    if new_total == 0:
        charge.status = "pending"
    elif new_total < charge.amount:
        charge.mark_as_partial()
    else:
        charge.mark_as_paid()

    charge.updated_at = datetime.utcnow()

    # guardar charge
    charge_repository.update(charge)

    return saved_payment

def void_payment(
    repository: PaymentRepository,
    charge_repository: ChargeRepository,
    payment_id: uuid.UUID,
    company_id: uuid.UUID,
    reason: str,
):
    # buscar pago
    payment = repository.get_by_id(payment_id)

    if not payment or payment.company_id != company_id:
        raise ValueError("Pago no encontrado")

    # anular (dominio)
    payment.void(reason)

    # guardar pago
    repository.update(payment)

    # obtener charge
    charge = charge_repository.get_by_id(
        payment.charge_id,
        company_id,
    )

    if not charge:
        raise ValueError("Cobro no encontrado")

    # recalcular total SIN este pago
    total_paid = repository.get_total_paid_by_charge(
        charge_id=charge.id,
        company_id=company_id,
    )

    # actualizar estado del charge
    if total_paid == 0:
        charge.status = "pending"
    elif total_paid < charge.amount:
        charge.mark_as_partial()
    else:
        charge.mark_as_paid()

    charge.updated_at = datetime.utcnow()

    # guardar
    charge_repository.update(charge)

    return payment