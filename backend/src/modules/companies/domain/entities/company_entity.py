# COMPANIES ENTITY

import uuid
from datetime import datetime


class Company:
    def __init__(
        self,
        name: str,
        email: str,
        tax_id: str,
        phone: str | None = None,
        status: str = "active",
        plan: str = "free",
        id: uuid.UUID | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ):
        # Validaciones básicas
        if not name:
            raise ValueError("El nombre de la Compañía es requerido")

        if not email:
            raise ValueError("El correo de la Compañía es requerido")

        if not tax_id:
            raise ValueError("El tax_id de la Compañía es requerido")

        if status not in ("active", "inactive"):
            raise ValueError("Estado Invalido")

        if plan not in ("free", "pro"):
            raise ValueError("Plan Invalido")

        # 🔹 Asignación
        self.id = id or uuid.uuid4()
        self.name = name
        self.email = email
        self.phone = phone
        self.tax_id = tax_id
        self.status = status
        self.plan = plan
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    # Métodos de negocio
    def activate(self):
        if self.status == "active":
            raise ValueError("La Compañía ya esta activa")
        self.status = "active"
        self._touch()

    def deactivate(self):
        if self.status == "inactive":
            raise ValueError("La Compañía ya esta inactiva")
        self.status = "inactive"
        self._touch()

    def upgrade_plan(self):
        if self.plan == "pro":
            raise ValueError("La Compañía ya esta en plan pro")
        self.plan = "pro"
        self._touch()

    # Método interno
    def _touch(self):
        self.updated_at = datetime.utcnow()