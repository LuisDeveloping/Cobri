# CLIENTS REPOSITORY (Interface)

from abc import ABC, abstractmethod
from typing import Optional, List
import uuid

from src.modules.clients.domain.entities.client_entity import Client

class ClientRepository(ABC):

    @abstractmethod
    def create(self, client: Client) -> Client:
        pass

    @abstractmethod
    def get_by_id(self, client_id: uuid.UUID, company_id: uuid.UUID) -> Optional[Client]:
        pass

    @abstractmethod
    def get_all(self, company_id: uuid.UUID) -> List[Client]:
        pass

    @abstractmethod
    def search(self, query: str, company_id: uuid.UUID) -> List[Client]:
        pass

    @abstractmethod
    def update(self, client: Client) -> Client:
        pass

    @abstractmethod
    def deactivate(self, client_id: uuid.UUID, company_id: uuid.UUID) -> None:
        pass