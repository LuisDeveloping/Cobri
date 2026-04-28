# CHARGES QUERIES
from typing import List, Optional
import uuid
from datetime import datetime

from src.modules.charges.domain.entities.charge_entity import Charge
from src.modules.charges.domain.interfaces.charge_repository import ChargeRepository

# GET ALL / FILTERED CHARGES
def get_charges(
    repository: ChargeRepository,
    company_id: uuid.UUID,
    status: Optional[str] = None,
    client_id: Optional[uuid.UUID] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
) -> List[Charge]:

    # si hay filtros → usar método dinámico
    if status or client_id or from_date or to_date:
        return repository.get_with_filters(
            company_id=company_id,
            status=status,
            client_id=client_id,
            from_date=from_date,
            to_date=to_date,
        )

    # si no hay filtros → traer todos
    return repository.get_all(company_id)


# GET CHARGE BY ID
def get_charge_by_id(
    repository: ChargeRepository,
    charge_id: uuid.UUID,
    company_id: uuid.UUID,
) -> Optional[Charge]:

    return repository.get_by_id(
        charge_id=charge_id,
        company_id=company_id,
    )