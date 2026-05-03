# PAYMENT ENTITY

import uuid
from datetime import datetime
from typing import Optional


class Payment:
    def __init__(
        self,
        charge_id: uuid.UUID,
        company_id: uuid.UUID,
        amount: float,
        payment_method: str,
        paid_at: datetime,
        reference: Optional[str] = None,
        status: str = "active",
        voided_at: Optional[datetime] = None,
        void_reason: Optional[str] = None,
        id: Optional[uuid.UUID] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        # VALIDACIONES

        if not charge_id:
            raise ValueError("El charge_id es requerido")

        if not company_id:
            raise ValueError("El company_id es requerido")

        if amount <= 0:
            raise ValueError("El monto debe ser mayor a 0")

        if payment_method not in ("cash", "transfer", "sinpe", "card"):
            raise ValueError("Método de pago inválido")

        if not paid_at:
            raise ValueError("La fecha de pago es requerida")

        if status not in ("active", "voided"):
            raise ValueError("Estado inválido")

        # regla importante
        if status == "voided" and not void_reason:
            raise ValueError("Debe indicar el motivo de anulación")

        # ASIGNACIÓN

        self.id = id or uuid.uuid4()
        self.charge_id = charge_id
        self.company_id = company_id
        self.amount = amount
        self.payment_method = payment_method
        self.reference = reference
        self.status = status
        self.paid_at = paid_at
        self.voided_at = voided_at
        self.void_reason = void_reason
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    # MÉTODOS DE NEGOCIO

    def void(self, reason: str):
        if self.status == "voided":
            raise ValueError("El pago ya está anulado")

        if not reason:
            raise ValueError("Debe indicar el motivo de anulación")

        self.status = "voided"
        self.void_reason = reason
        self.voided_at = datetime.utcnow()
        self._touch()

    # Método interno
    def _touch(self):
        self.updated_at = datetime.utcnow()