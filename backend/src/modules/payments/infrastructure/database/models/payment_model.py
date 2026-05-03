# PAYMENTS ORM MODEL

import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database.session import Base


class PaymentModel(Base):
    __tablename__ = "payments"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    charge_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("charges.id"),
        nullable=False
    )

    company_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("companies.id"),
        nullable=False
    )

    amount: Mapped[float] = mapped_column(
        Numeric(10, 2),  # importante para dinero
        nullable=False
    )

    payment_method: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    reference: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="active"
    )

    paid_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    voided_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )

    void_reason: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )