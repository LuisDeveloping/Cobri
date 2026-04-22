# CLIENTS REPOSITORY IMPLEMENTATION

from typing import Optional, List
import uuid

from sqlalchemy.orm import Session
from sqlalchemy import or_

from src.core.database.base_repository import BaseRepository
from src.modules.clients.domain.interfaces.client_repository import ClientRepository
from src.modules.clients.domain.entities.client_entity import Client
from src.modules.clients.infrastructure.database.models.client_model import ClientModel


class SqlAlchemyClientRepository(BaseRepository, ClientRepository):

    def __init__(self, db: Session):
        super().__init__(db, ClientModel)

    # CREATE CLIENT
    def create(self, client: Client) -> Client:
        client_model = ClientModel(
            id=client.id,
            name=client.name,
            phone=client.phone,
            email=client.email,
            identification=client.identification,
            notes=client.notes,
            company_id=client.company_id,
            status=client.status,
            created_at=client.created_at,
            updated_at=client.updated_at,
        )

        saved_client = super().create(client_model)
        return self._to_entity(saved_client)

    # GET CLIENT BY ID (MULTI-TENANT SEGURO)
    def get_by_id(self, client_id: uuid.UUID, company_id: uuid.UUID) -> Optional[Client]:
        client = self.db.query(ClientModel).filter(
            ClientModel.id == client_id,
            ClientModel.company_id == company_id
        ).first()

        if not client:
            return None

        return self._to_entity(client)

    # GET ALL CLIENTS BY COMPANY
    def get_all(self, company_id: uuid.UUID) -> List[Client]:
        clients = self.db.query(ClientModel).filter(
            ClientModel.company_id == company_id,
            ClientModel.status == "active"
        ).all()

        return [self._to_entity(c) for c in clients]

    # SEARCH CLIENTS (nombre o teléfono)
    def search(self, query: str, company_id: uuid.UUID) -> List[Client]:
        clients = self.db.query(ClientModel).filter(
            ClientModel.company_id == company_id,
            ClientModel.status == "active",
            or_(
                ClientModel.name.ilike(f"%{query}%"),
                ClientModel.phone.ilike(f"%{query}%")
            )
        ).all()

        return [self._to_entity(c) for c in clients]

    # UPDATE CLIENT
    def update(self, client: Client) -> Client:
        client_model = self.db.query(ClientModel).filter(
            ClientModel.id == client.id,
            ClientModel.company_id == client.company_id
        ).first()

        if not client_model:
            return None

        client_model.name = client.name
        client_model.phone = client.phone
        client_model.email = client.email
        client_model.identification = client.identification
        client_model.notes = client.notes
        client_model.status = client.status
        client_model.updated_at = client.updated_at

        self.db.commit()
        self.db.refresh(client_model)

        return self._to_entity(client_model)

    # DEACTIVATE CLIENT (SOFT DELETE REAL)
    def deactivate(self, client_id: uuid.UUID, company_id: uuid.UUID) -> None:
        client_model = self.db.query(ClientModel).filter(
            ClientModel.id == client_id,
            ClientModel.company_id == company_id
        ).first()

        if not client_model:
            return None

        client_model.status = "inactive"

        self.db.commit()

    # 🔹 Mapper interno
    def _to_entity(self, model: ClientModel) -> Client:
        return Client(
            id=model.id,
            name=model.name,
            phone=model.phone,
            email=model.email,
            identification=model.identification,
            notes=model.notes,
            company_id=model.company_id,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )