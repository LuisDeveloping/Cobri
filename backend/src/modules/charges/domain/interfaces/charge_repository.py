# CHARGE REPOSITORY (Interface)

from abc import ABC, abstractmethod
from typing import Optional, List
import uuid
from datetime import datetime

from src.modules.charges.domain.entities.charge_entity import Charge


class ChargeRepository(ABC):

    @abstractmethod
    def create(self, charge: Charge) -> Charge:
        pass

    @abstractmethod
    def get_by_id(self, charge_id: uuid.UUID, company_id: uuid.UUID) -> Optional[Charge]:
        pass

    @abstractmethod
    def get_all(self, company_id: uuid.UUID) -> List[Charge]:
        pass

    @abstractmethod
    def get_with_filters(
        self,
        company_id: uuid.UUID,
        status: Optional[str] = None,
        client_id: Optional[uuid.UUID] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> List[Charge]:
        pass

    @abstractmethod
    def update(self, charge: Charge) -> Charge:
        pass