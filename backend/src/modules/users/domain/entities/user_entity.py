# USERS ENTITY

import uuid
from datetime import datetime
from typing import Optional


class User:
    def __init__(
        self,
        name: str,
        email: str,
        password_hash: str,
        role: str,
        company_id: uuid.UUID,
        status: str = "active",
        id: Optional[uuid.UUID] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        # Validaciones básicas
        if not name:
            raise ValueError("El nombre del usuario es requerido")

        if not email:
            raise ValueError("El correo del usuario es requerido")

        if not password_hash:
            raise ValueError("La contraseña es requerida")

        if role not in ("owner", "admin", "staff"):
            raise ValueError("Rol inválido")

        if not company_id:
            raise ValueError("El company_id es requerido")

        if status not in ("active", "inactive"):
            raise ValueError("Estado inválido")

        # Asignación
        self.id = id or uuid.uuid4()
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.company_id = company_id
        self.status = status
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    # Métodos de negocio

    def activate(self):
        if self.status == "active":
            raise ValueError("El usuario ya está activo")
        self.status = "active"
        self._touch()

    def deactivate(self):
        if self.status == "inactive":
            raise ValueError("El usuario ya está inactivo")
        self.status = "inactive"
        self._touch()

    def change_role(self, new_role: str):
        if new_role not in ("owner", "admin", "staff"):
            raise ValueError("Rol inválido")

        if self.role == new_role:
            raise ValueError("El usuario ya tiene ese rol")

        self.role = new_role
        self._touch()

    # 🔹 Método interno
    def _touch(self):
        self.updated_at = datetime.utcnow()