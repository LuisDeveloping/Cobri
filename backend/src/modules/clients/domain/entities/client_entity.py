# CLIENTS ENTITY

import uuid
from datetime import datetime
from typing import Optional


class Client:
    def __init__(
        self,
        name: str,
        phone: str,
        company_id: uuid.UUID,
        email: Optional[str] = None,
        identification: Optional[str] = None,
        notes: Optional[str] = None,
        status: str = "active",
        id: Optional[uuid.UUID] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        # Validaciones

        if not name or not name.strip():
            raise ValueError("El nombre del cliente es requerido")

        if not phone or len(phone.strip()) < 8:
            raise ValueError("El número de teléfono es inválido")

        if email and "@" not in email:
            raise ValueError("Correo inválido")

        if not company_id:
            raise ValueError("El company_id es requerido")

        if status not in ("active", "inactive"):
            raise ValueError("Estado inválido")

        # Normalización de datos
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip() if email else None
        self.identification = identification.strip() if identification else None
        self.notes = notes.strip() if notes else None

        # Asignación
        self.id = id or uuid.uuid4()
        self.company_id = company_id
        self.status = status
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    # MÉTODOS DE NEGOCIO
    def activate(self):
        if self.status == "active":
            raise ValueError("El cliente ya está activo")
        self.status = "active"
        self._touch()

    def deactivate(self):
        if self.status == "inactive":
            raise ValueError("El cliente ya está inactivo")
        self.status = "inactive"
        self._touch()

    def update_info(
        self,
        name: str,
        phone: str,
        email: Optional[str] = None,
        identification: Optional[str] = None,
        notes: Optional[str] = None,
    ):
        
        # Validaciones iguales al constructor
        if not name or not name.strip():
            raise ValueError("El nombre del cliente es requerido")

        if not phone or len(phone.strip()) < 8:
            raise ValueError("El número de teléfono es inválido")

        if email and "@" not in email:
            raise ValueError("Correo inválido")

        # Actualización
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip() if email else None
        self.identification = identification.strip() if identification else None
        self.notes = notes.strip() if notes else None

        self._touch()

    # MÉTODO INTERNO
    def _touch(self):
        self.updated_at = datetime.utcnow()