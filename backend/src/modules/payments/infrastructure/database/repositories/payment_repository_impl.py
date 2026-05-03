# PAYMENT REPOSITORY IMPLEMENTATION

from typing import Optional, List
import uuid

from sqlalchemy.orm import Session
from sqlalchemy import func

from src.core.database.base_repository import BaseRepository
from src.modules.payments.domain.interfaces.payment_repository import PaymentRepository
from src.modules.payments.domain.entities.payment_entity import Payment
from src.modules.payments.infrastructure.database.models.payment_model import PaymentModel


class SqlAlchemyPaymentRepository(BaseRepository, PaymentRepository):

    def __init__(self, db: Session):
        super().__init__(db, PaymentModel)

    # CREATE
    def create(self, payment: Payment) -> Payment:
        payment_model = PaymentModel(
            id=payment.id,
            charge_id=payment.charge_id,
            company_id=payment.company_id,
            amount=payment.amount,
            payment_method=payment.payment_method,
            reference=payment.reference,
            status=payment.status,
            paid_at=payment.paid_at,
            voided_at=payment.voided_at,
            void_reason=payment.void_reason,
            created_at=payment.created_at,
            updated_at=payment.updated_at,
        )

        saved_payment = super().create(payment_model)

        return self._to_entity(saved_payment)

    # GET BY ID
    def get_by_id(self, payment_id: uuid.UUID) -> Optional[Payment]:
        payment_model = super().get_by_id(payment_id)

        if not payment_model:
            return None

        return self._to_entity(payment_model)

    # GET PAYMENTS BY CHARGE (HISTORIAL)
    def get_by_charge_id(
        self,
        charge_id: uuid.UUID,
        company_id: uuid.UUID,
    ) -> List[Payment]:

        payments = (
            self.db.query(PaymentModel)
            .filter(
                PaymentModel.charge_id == charge_id,
                PaymentModel.company_id == company_id,
                PaymentModel.status == "active",  # importante
            )
            .order_by(PaymentModel.paid_at.asc())
            .all()
        )

        return [self._to_entity(p) for p in payments]

    # GET TOTAL PAID BY CHARGE
    def get_total_paid_by_charge(
        self,
        charge_id: uuid.UUID,
        company_id: uuid.UUID,
    ) -> float:

        total = (
            self.db.query(func.sum(PaymentModel.amount))
            .filter(
                PaymentModel.charge_id == charge_id,
                PaymentModel.company_id == company_id,
                PaymentModel.status == "active",  # ignorar anulados
            )
            .scalar()
        )

        return float(total or 0.0)  # evitar None

    # UPDATE (para void)
    def update(self, payment: Payment) -> Payment:
        payment_model = (
            self.db.query(PaymentModel)
            .filter(PaymentModel.id == payment.id)
            .first()
        )

        if not payment_model:
            return None

        payment_model.status = payment.status
        payment_model.voided_at = payment.voided_at
        payment_model.void_reason = payment.void_reason
        payment_model.updated_at = payment.updated_at

        self.db.commit()
        self.db.refresh(payment_model)

        return self._to_entity(payment_model)

    # MAPPER
    def _to_entity(self, model: PaymentModel) -> Payment:
        return Payment(
            id=model.id,
            charge_id=model.charge_id,
            company_id=model.company_id,
            amount=model.amount,
            payment_method=model.payment_method,
            reference=model.reference,
            status=model.status,
            paid_at=model.paid_at,
            voided_at=model.voided_at,
            void_reason=model.void_reason,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )