# CHARGE REPOSITORY IMPLEMENTATION

from typing import Optional, List
import uuid
from datetime import datetime

from sqlalchemy.orm import Session

from src.core.database.base_repository import BaseRepository
from src.modules.charges.domain.interfaces.charge_repository import ChargeRepository
from src.modules.charges.domain.entities.charge_entity import Charge
from src.modules.charges.infrastructure.database.models.charge_model import ChargeModel


class SqlAlchemyChargeRepository(BaseRepository, ChargeRepository):

    def __init__(self, db: Session):
        super().__init__(db, ChargeModel)

    # CREATE CHARGE
    def create(self, charge: Charge) -> Charge:
        charge_model = ChargeModel(
            id=charge.id,
            company_id=charge.company_id,
            client_id=charge.client_id,
            amount=charge.amount,
            description=charge.description,
            charge_date=charge.charge_date,
            due_date=charge.due_date,
            status=charge.status,
            paid_at=charge.paid_at,
            created_at=charge.created_at,
            updated_at=charge.updated_at,
        )

        saved_charge = super().create(charge_model)

        return self._to_entity(saved_charge)

    # GET BY ID (multi-tenant seguro)
    def get_by_id(
        self,
        charge_id: uuid.UUID,
        company_id: uuid.UUID,
    ) -> Optional[Charge]:

        charge_model = (
            self.db.query(ChargeModel)
            .filter(
                ChargeModel.id == charge_id,
                ChargeModel.company_id == company_id,
            )
            .first()
        )

        if not charge_model:
            return None

        return self._to_entity(charge_model)

    # GET ALL
    def get_all(self, company_id: uuid.UUID) -> List[Charge]:
        charges = (
            self.db.query(ChargeModel)
            .filter(ChargeModel.company_id == company_id)
            .all()
        )

        return [self._to_entity(charge) for charge in charges]

    # GET WITH FILTERS
    def get_with_filters(
        self,
        company_id: uuid.UUID,
        status: Optional[str] = None,
        client_id: Optional[uuid.UUID] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
    ) -> List[Charge]:

        query = self.db.query(ChargeModel)

        # multi-tenant SIEMPRE primero
        query = query.filter(ChargeModel.company_id == company_id)

        # filtros dinámicos
        if status:
            query = query.filter(ChargeModel.status == status)

        if client_id:
            query = query.filter(ChargeModel.client_id == client_id)

        if from_date:
            query = query.filter(ChargeModel.charge_date >= from_date)

        if to_date:
            query = query.filter(ChargeModel.charge_date <= to_date)

        charges = query.all()

        return [self._to_entity(charge) for charge in charges]

    # UPDATE
    def update(self, charge: Charge) -> Charge:
        charge_model = (
            self.db.query(ChargeModel)
            .filter(ChargeModel.id == charge.id)
            .first()
        )

        if not charge_model:
            return None

        charge_model.description = charge.description
        charge_model.due_date = charge.due_date
        charge_model.status = charge.status
        charge_model.paid_at = charge.paid_at
        charge_model.updated_at = charge.updated_at

        self.db.commit()
        self.db.refresh(charge_model)

        return self._to_entity(charge_model)

    # Mapper interno
    def _to_entity(self, charge_model: ChargeModel) -> Charge:
        return Charge(
            id=charge_model.id,
            company_id=charge_model.company_id,
            client_id=charge_model.client_id,
            amount=charge_model.amount,
            description=charge_model.description,
            charge_date=charge_model.charge_date,
            due_date=charge_model.due_date,
            status=charge_model.status,
            paid_at=charge_model.paid_at,
            created_at=charge_model.created_at,
            updated_at=charge_model.updated_at,
        )