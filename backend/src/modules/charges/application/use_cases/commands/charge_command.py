# CHARGE COMMANDS
from datetime import datetime
import uuid

from src.modules.charges.domain.entities.charge_entity import Charge
from src.modules.charges.domain.interfaces.charge_repository import ChargeRepository
from src.modules.clients.domain.interfaces.client_repository import ClientRepository

def create_charge(
    repository: ChargeRepository,
    client_repository: ClientRepository,
    client_id,
    amount,
    description,
    charge_date,
    due_date,
    company_id,
):
    # validar cliente dentro del tenant
    client = client_repository.get_by_id(client_id, company_id)

    if not client:
        raise ValueError("Cliente no encontrado")

    # crear entidad (aplica reglas del dominio)
    charge = Charge(
        client_id=client_id,
        company_id=company_id,
        amount=amount,
        description=description,
        charge_date=charge_date,
        due_date=due_date,
    )

    # guardar
    return repository.create(charge)

def update_charge(
    repository: ChargeRepository,
    charge_id: uuid.UUID,
    company_id: uuid.UUID,
    description: str,
    due_date,
):
    # buscar cobro (multi-tenant)
    charge = repository.get_by_id(charge_id, company_id)

    if not charge:
        raise ValueError("Cobro no encontrado")

    # reglas de negocio
    if charge.status in ("paid", "cancelled"):
        raise ValueError("No se puede editar un cobro cerrado")

    # actualizar campos permitidos
    charge.description = description
    charge.due_date = due_date
    charge.updated_at = datetime.utcnow()

    # guardar
    return repository.update(charge)

def cancel_charge(
    repository: ChargeRepository,
    charge_id: uuid.UUID,
    company_id: uuid.UUID,
):
    # buscar
    charge = repository.get_by_id(charge_id, company_id)

    if not charge:
        raise ValueError("Cobro no encontrado")

    # reglas
    if charge.status == "paid":
        raise ValueError("No se puede cancelar un cobro pagado")

    if charge.status == "cancelled":
        raise ValueError("El cobro ya está cancelado")

    # cambio de estado
    charge.status = "cancelled"
    charge.updated_at = datetime.utcnow()

    # guardar
    repository.update(charge)