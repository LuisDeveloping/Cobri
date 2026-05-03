# PAYMENT REPOSITORY (INTERFACE)

from abc import ABC, abstractmethod
from typing import List, Optional
import uuid

from src.modules.payments.domain.entities.payment_entity import Payment


class PaymentRepository(ABC):

    @abstractmethod
    def create(self, payment: Payment) -> Payment:
        pass

    @abstractmethod
    def get_by_id(self, payment_id: uuid.UUID) -> Optional[Payment]:
        pass

    @abstractmethod
    def get_by_charge_id(
        self,
        charge_id: uuid.UUID,
        company_id: uuid.UUID,
    ) -> List[Payment]:
        pass

    @abstractmethod
    def get_total_paid_by_charge(
        self,
        charge_id: uuid.UUID,
        company_id: uuid.UUID,
    ) -> float:
        pass

    @abstractmethod
    def update(self, payment: Payment) -> Payment:
        pass