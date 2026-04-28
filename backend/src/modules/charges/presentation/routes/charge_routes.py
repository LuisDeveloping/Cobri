# CHARGES ROUTES

from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
import uuid
from datetime import datetime

from src.core.dependecies.charge_dependencies import get_charge_repository
from src.core.dependecies.client_dependencies import get_client_repository
from src.core.dependecies.auth_dependencies import get_current_user
from src.core.dependecies.role_dependencies import require_roles
from src.core.dependecies.audit_dependencies import get_audit_repository

from src.modules.charges.application.use_cases.commands.charge_command import (create_charge, update_charge, cancel_charge,)
from src.modules.charges.application.use_cases.queries.charge_query import (get_charges, get_charge_by_id,)
from src.modules.charges.presentation.schemas.charge_schema import (CreateChargeRequest, UpdateChargeRequest, ChargeResponse,)

router = APIRouter(prefix="/charges", tags=["Charges"])

@router.post("/", response_model=ChargeResponse)
def create_charge_route(
    request: CreateChargeRequest,
    repository=Depends(get_charge_repository),
    client_repository=Depends(get_client_repository),
    audit_repo=Depends(get_audit_repository),
    current_user=Depends(require_roles(["admin", "owner"])),
):
    try:
        charge = create_charge(
            repository=repository,
            client_repository=client_repository,
            client_id=request.client_id,
            amount=request.amount,
            description=request.description,
            charge_date=request.charge_date,
            due_date=request.due_date,
            company_id=current_user.company_id,
        )

        audit_repo.create_log(
            user_id=current_user.id,
            action="CREATE",
            entity="Charge",
            entity_id=charge.id,
        )

        return charge

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[ChargeResponse])
def get_charges_route(
    status: Optional[str] = None,
    client_id: Optional[uuid.UUID] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    repository=Depends(get_charge_repository),
    current_user=Depends(get_current_user),
):
    return get_charges(
        repository=repository,
        company_id=current_user.company_id,
        status=status,
        client_id=client_id,
        from_date=from_date,
        to_date=to_date,
    )

@router.get("/{charge_id}", response_model=ChargeResponse)
def get_charge_by_id_route(
    charge_id: uuid.UUID,
    repository=Depends(get_charge_repository),
    current_user=Depends(get_current_user),
):
    charge = get_charge_by_id(
        repository=repository,
        charge_id=charge_id,
        company_id=current_user.company_id,
    )

    if not charge:
        raise HTTPException(status_code=404, detail="Cobro no encontrado")

    return charge

@router.put("/{charge_id}", response_model=ChargeResponse)
def update_charge_route(
    charge_id: uuid.UUID,
    request: UpdateChargeRequest,
    repository=Depends(get_charge_repository),
    audit_repo=Depends(get_audit_repository),
    current_user=Depends(require_roles(["admin", "owner"])),
):
    try:
        charge = update_charge(
            repository=repository,
            charge_id=charge_id,
            company_id=current_user.company_id,
            description=request.description,
            due_date=request.due_date,
        )

        audit_repo.create_log(
            user_id=current_user.id,
            action="UPDATE",
            entity="Charge",
            entity_id=charge.id,
        )

        return charge

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{charge_id}", status_code=204)
def cancel_charge_route(
    charge_id: uuid.UUID,
    repository=Depends(get_charge_repository),
    audit_repo=Depends(get_audit_repository),
    current_user=Depends(require_roles(["admin", "owner"])),
):
    try:
        cancel_charge(
            repository=repository,
            charge_id=charge_id,
            company_id=current_user.company_id,
        )

        audit_repo.create_log(
            user_id=current_user.id,
            action="CANCEL",
            entity="Charge",
            entity_id=charge_id,
        )

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))