# CHARGE ENTITY

import uuid
from datetime import datetime
from typing import Optional


class Charge:
    def __init__(
        self,
        company_id: uuid.UUID,
        client_id: uuid.UUID,
        amount: float,
        description: str,
        charge_date: datetime,
        due_date: Optional[datetime] = None,
        status: str = "pending",
        paid_at: Optional[datetime] = None,
        id: Optional[uuid.UUID] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        # Validaciones básicas

        if not company_id:
            raise ValueError("El company_id es requerido")

        if not client_id:
            raise ValueError("El client_id es requerido")

        if amount <= 0:
            raise ValueError("El monto debe ser mayor a 0")

        if not description:
            raise ValueError("La descripción es requerida")

        if not charge_date:
            raise ValueError("La fecha del cobro es requerida")

        if status not in ("pending", "partial", "paid", "cancelled"):
            raise ValueError("Estado inválido")

        # Asignación

        self.id = id or uuid.uuid4()
        self.company_id = company_id
        self.client_id = client_id
        self.amount = amount
        self.description = description
        self.charge_date = charge_date
        self.due_date = due_date
        self.status = status
        self.paid_at = paid_at
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    # MÉTODOS DE NEGOCIO
    def mark_as_paid(self):
        if self.status == "paid":
            raise ValueError("El cobro ya está pagado")

        if self.status == "cancelled":
            raise ValueError("No se puede pagar un cobro cancelado")

        self.status = "paid"
        self.paid_at = datetime.utcnow()
        self._touch()

    def mark_as_partial(self):
        if self.status in ("paid", "cancelled"):
            raise ValueError("No se puede marcar como parcial")

        self.status = "partial"
        self._touch()

    def cancel(self):
        if self.status == "paid":
            raise ValueError("No se puede cancelar un cobro pagado")

        if self.status == "cancelled":
            raise ValueError("El cobro ya está cancelado")

        self.status = "cancelled"
        self._touch()

    def update_data(
        self,
        description: str,
        due_date: Optional[datetime],
    ):
        if self.status in ("paid", "cancelled"):
            raise ValueError("No se puede editar un cobro cerrado")

        if not description:
            raise ValueError("La descripción es requerida")

        self.description = description
        self.due_date = due_date
        self._touch()
        
    # Método interno
    def _touch(self):
        self.updated_at = datetime.utcnow()
    
