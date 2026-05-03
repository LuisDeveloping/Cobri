# PAYMENTS ROUTES

from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid

from src.core.dependecies.payment_dependencies import get_payment_repository
from src.core.dependecies.charge_dependencies import get_charge_repository
from src.core.dependecies.auth_dependencies import get_current_user
from src.core.dependecies.role_dependencies import require_roles
from src.core.dependecies.audit_dependencies import get_audit_repository

from src.modules.payments.application.use_cases.commands.payment_command import (
    create_payment,
    void_payment,
)
from src.modules.payments.application.use_cases.queries.payment_query import (
    get_payments_by_charge,
    get_payment_by_id,
)
from src.modules.payments.presentation.schemas.payment_schema import (
    CreatePaymentRequest,
    VoidPaymentRequest,
    PaymentResponse,
)

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=PaymentResponse)
def create_payment_route(
    request: CreatePaymentRequest,
    repository=Depends(get_payment_repository),
    charge_repository=Depends(get_charge_repository),
    audit_repo=Depends(get_audit_repository),
    current_user=Depends(require_roles(["admin", "owner"])),
):
    try:
        payment = create_payment(
            repository=repository,
            charge_repository=charge_repository,
            charge_id=request.charge_id,
            amount=request.amount,
            payment_method=request.payment_method,
            paid_at=request.paid_at,
            reference=request.reference,
            company_id=current_user.company_id,
        )

        audit_repo.create_log(
            user_id=current_user.id,
            action="CREATE",
            entity="Payment",
            entity_id=payment.id,
        )

        return payment

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/charge/{charge_id}", response_model=List[PaymentResponse])
def get_payments_by_charge_route(
    charge_id: uuid.UUID,
    repository=Depends(get_payment_repository),
    current_user=Depends(get_current_user),
):
    return get_payments_by_charge(
        repository=repository,
        charge_id=charge_id,
        company_id=current_user.company_id,
    )

@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment_by_id_route(
    payment_id: uuid.UUID,
    repository=Depends(get_payment_repository),
    current_user=Depends(get_current_user),
):
    payment = get_payment_by_id(
        repository=repository,
        payment_id=payment_id,
        company_id=current_user.company_id,
    )

    if not payment:
        raise HTTPException(status_code=404, detail="Pago no encontrado")

    return payment

@router.put("/{payment_id}/void", response_model=PaymentResponse)
def void_payment_route(
    payment_id: uuid.UUID,
    request: VoidPaymentRequest,
    repository=Depends(get_payment_repository),
    charge_repository=Depends(get_charge_repository),
    audit_repo=Depends(get_audit_repository),
    current_user=Depends(require_roles(["admin", "owner"])),
):
    try:
        payment = void_payment(
            repository=repository,
            charge_repository=charge_repository,
            payment_id=payment_id,
            company_id=current_user.company_id,
            reason=request.reason,
        )

        audit_repo.create_log(
            user_id=current_user.id,
            action="VOID",
            entity="Payment",
            entity_id=payment.id,
        )

        return payment

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))