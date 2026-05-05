# NOTIFICATION ENTITY

import uuid
from datetime import datetime
from typing import Optional


class Notification:
    def __init__(
        self,
        company_id: uuid.UUID,
        type: str,
        message: str,
        channel: str,
        status: str = "pending",
        client_id: Optional[uuid.UUID] = None,
        user_id: Optional[uuid.UUID] = None,
        charge_id: Optional[uuid.UUID] = None,
        sent_at: Optional[datetime] = None,
        id: Optional[uuid.UUID] = None,
        created_at: Optional[datetime] = None,
    ):
        # Validaciones básicas

        if not company_id:
            raise ValueError("El company_id es requerido")

        if not message:
            raise ValueError("El mensaje es requerido")

        if type not in ("payment_reminder", "payment_received", "charge_overdue"):
            raise ValueError("Tipo de notificación inválido")

        if channel not in ("email", "whatsapp", "internal"):
            raise ValueError("Canal inválido")

        if status not in ("pending", "sent", "failed"):
            raise ValueError("Estado inválido")

        # Regla importante (mínimo un destino)
        if not client_id and not user_id:
            raise ValueError("La notificación debe tener un destino (client_id o user_id)")

        # Asignación

        self.id = id or uuid.uuid4()
        self.company_id = company_id
        self.client_id = client_id
        self.user_id = user_id
        self.charge_id = charge_id
        self.type = type
        self.message = message
        self.channel = channel
        self.status = status
        self.sent_at = sent_at
        self.created_at = created_at or datetime.utcnow()

    # ======================
    # MÉTODOS DE NEGOCIO
    # ======================

    def mark_as_sent(self):
        if self.status == "sent":
            raise ValueError("La notificación ya fue enviada")

        self.status = "sent"
        self.sent_at = datetime.utcnow()

    def mark_as_failed(self):
        if self.status == "failed":
            raise ValueError("La notificación ya está marcada como fallida")

        self.status = "failed"