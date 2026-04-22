# CLIENTS QUERIES

from typing import List, Optional
import uuid

from src.modules.clients.domain.entities.client_entity import Client
from src.modules.clients.domain.interfaces.client_repository import ClientRepository


# GET ALL CLIENTS
def get_all_clients(
    repository: ClientRepository,
    company_id: uuid.UUID,
) -> List[Client]:
    return repository.get_all(company_id)


# GET CLIENT BY ID
def get_client_by_id(
    repository: ClientRepository,
    client_id: uuid.UUID,
    company_id: uuid.UUID,
) -> Optional[Client]:
    return repository.get_by_id(client_id, company_id)


# SEARCH CLIENTS
def search_clients(
    repository: ClientRepository,
    query: str,
    company_id: uuid.UUID,
) -> List[Client]:
    return repository.search(query, company_id)