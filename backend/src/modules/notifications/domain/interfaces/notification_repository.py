# NOTIFICATION REPOSITORY (Interface)

from abc import ABC, abstractmethod
from typing import List, Optional
import uuid

from src.modules.notifications.domain.entities.notification_entity import Notification


class NotificationRepository(ABC):

    @abstractmethod
    def create(self, notification: Notification) -> Notification:
        pass

    @abstractmethod
    def get_by_id(self, notification_id: uuid.UUID) -> Optional[Notification]:
        pass

    @abstractmethod
    def get_by_company(self, company_id: uuid.UUID) -> List[Notification]:
        pass

    @abstractmethod
    def get_by_client(self, client_id: uuid.UUID, company_id: uuid.UUID) -> List[Notification]:
        pass

    @abstractmethod
    def get_by_charge(self, charge_id: uuid.UUID, company_id: uuid.UUID) -> List[Notification]:
        pass