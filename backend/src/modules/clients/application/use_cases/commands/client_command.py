# CREATE CLIENT

from typing import Optional
import uuid

from src.modules.clients.domain.entities.client_entity import Client
from src.modules.clients.domain.interfaces.client_repository import ClientRepository

def create_client(
    repository: ClientRepository,
    name: str,
    phone: str,
    company_id: uuid.UUID,
    email: str = None,
    identification: str = None,
    notes: str = None,
):
    # Crear entidad (valida dominio)
    client = Client(
        name=name,
        phone=phone,
        email=email,
        identification=identification,
        notes=notes,
        company_id=company_id,
    )

    return repository.create(client)

# UPDATE CLIENT

def update_client(
    repository: ClientRepository,
    client_id: uuid.UUID,
    company_id: uuid.UUID,
    name: str,
    phone: str,
    email: str = None,
    identification: str = None,
    notes: str = None,
):
    # Buscar cliente
    client = repository.get_by_id(client_id, company_id)

    if not client:
        raise ValueError("Cliente no encontrado")

    # usamos método de dominio (NO asignación directa)
    client.update_info(
        name=name,
        phone=phone,
        email=email,
        identification=identification,
        notes=notes,
    )

    return repository.update(client)

# DEACTIVATE CLIENT

def deactivate_client(
    repository: ClientRepository,
    client_id: uuid.UUID,
    company_id: uuid.UUID,
):
    # Buscar cliente
    client = repository.get_by_id(client_id, company_id)

    if not client:
        raise ValueError("Cliente no encontrado")

    # lógica de dominio
    client.deactivate()

    # Persistir
    repository.update(client)