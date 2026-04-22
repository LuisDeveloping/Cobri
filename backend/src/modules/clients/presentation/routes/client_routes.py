# CLIENTS ROUTES

from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid

from src.core.dependecies.client_dependencies import get_client_repository
from src.core.dependecies.auth_dependencies import get_current_user
from src.core.dependecies.role_dependencies import require_roles
from src.core.dependecies.audit_dependencies import get_audit_repository

from src.modules.clients.application.use_cases.commands.client_command import (create_client, update_client, deactivate_client,)
from src.modules.clients.application.use_cases.queries.client_query import (get_all_clients, get_client_by_id, search_clients,)
from src.modules.clients.presentation.schemas.client_schema import (CreateClientRequest,UpdateClientRequest,ClientResponse,)

router = APIRouter(prefix="/clients", tags=["Clients"])

# GET/clients/Get All Clients Route
@router.get("/", response_model=List[ClientResponse])
def get_all_clients_route(
    repository=Depends(get_client_repository),
    current_user=Depends(get_current_user),
):
    return get_all_clients(
        repository=repository,
        company_id=current_user.company_id,
    )

# GET/clients/Get Clients Route
@router.get("/", response_model=List[ClientResponse])
def get_clients_route(
    q: str = None,
    repository=Depends(get_client_repository),
    current_user=Depends(get_current_user),
):
    if q:
        return search_clients(
            repository=repository,
            query=q,
            company_id=current_user.company_id,
        )

    return get_all_clients(
        repository=repository,
        company_id=current_user.company_id,
    )

# GET/clients/{client_id}/Get Client By Id Route
@router.get("/{client_id}", response_model=ClientResponse)
def get_client_by_id_route(
    client_id: uuid.UUID,
    repository=Depends(get_client_repository),
    current_user=Depends(get_current_user),
):
    client = get_client_by_id(
        repository=repository,
        client_id=client_id,
        company_id=current_user.company_id,
    )

    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    return client

# POST/clients/Create Client Route
@router.post("/", response_model=ClientResponse)
def create_client_route(
    request: CreateClientRequest,
    repository=Depends(get_client_repository),
    audit_repo=Depends(get_audit_repository),
    current_user=Depends(require_roles(["admin", "owner"])),
):
    try:
        client = create_client(
            repository=repository,
            name=request.name,
            phone=request.phone,
            email=request.email,
            identification=request.identification,
            notes=request.notes,
            company_id=current_user.company_id,  # seguro
        )

        audit_repo.create_log(
            user_id=current_user.id,
            action="CREATE",
            entity="Client",
            entity_id=client.id,
        )

        return client

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# PUT/clients/{client_id}/Update Client Route
@router.put("/{client_id}", response_model=ClientResponse)
def update_client_route(
    client_id: uuid.UUID,
    request: UpdateClientRequest,
    repository=Depends(get_client_repository),
    audit_repo=Depends(get_audit_repository),
    current_user=Depends(require_roles(["admin", "owner"])),
):
    try:
        client = update_client(
            repository=repository,
            client_id=client_id,
            company_id=current_user.company_id,
            name=request.name,
            phone=request.phone,
            email=request.email,
            identification=request.identification,
            notes=request.notes,
        )

        audit_repo.create_log(
            user_id=current_user.id,
            action="UPDATE",
            entity="Client",
            entity_id=client.id,
        )

        return client

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# DELETE/clients/{client_id}/Delete Client Route
@router.delete("/{client_id}", status_code=204)
def delete_client_route(
    client_id: uuid.UUID,
    repository=Depends(get_client_repository),
    audit_repo=Depends(get_audit_repository),
    current_user=Depends(require_roles(["admin", "owner"])),
):
    try:
        deactivate_client(
            repository=repository,
            client_id=client_id,
            company_id=current_user.company_id,
        )

        audit_repo.create_log(
            user_id=current_user.id,
            action="DEACTIVATE",
            entity="Client",
            entity_id=client_id,
        )

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))