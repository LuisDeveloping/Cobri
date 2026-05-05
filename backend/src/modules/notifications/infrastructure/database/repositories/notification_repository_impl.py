# NOTIFICATION REPOSITORY IMPLEMENTATION

from typing import Optional, List
import uuid

from sqlalchemy.orm import Session

from src.core.database.base_repository import BaseRepository
from src.modules.notifications.domain.interfaces.notification_repository import NotificationRepository
from src.modules.notifications.domain.entities.notification_entity import Notification
from src.modules.notifications.infrastructure.database.models.notification_model import NotificationModel


class SqlAlchemyNotificationRepository(BaseRepository, NotificationRepository):

    def __init__(self, db: Session):
        super().__init__(db, NotificationModel)

    # CREATE
    def create(self, notification: Notification) -> Notification:
        notification_model = NotificationModel(
            id=notification.id,
            company_id=notification.company_id,
            client_id=notification.client_id,
            user_id=notification.user_id,
            charge_id=notification.charge_id,
            type=notification.type,
            message=notification.message,
            channel=notification.channel,
            status=notification.status,
            sent_at=notification.sent_at,
            created_at=notification.created_at,
        )

        saved = super().create(notification_model)

        return self._to_entity(saved)

    # GET BY ID
    def get_by_id(self, notification_id: uuid.UUID) -> Optional[Notification]:
        model = super().get_by_id(notification_id)

        if not model:
            return None

        return self._to_entity(model)

    # GET BY COMPANY (multi-tenant base)
    def get_by_company(self, company_id: uuid.UUID) -> List[Notification]:
        notifications = self.db.query(NotificationModel).filter(
            NotificationModel.company_id == company_id
        ).order_by(NotificationModel.created_at.desc()).all()

        return [self._to_entity(n) for n in notifications]

    # GET BY CLIENT
    def get_by_client(self, client_id: uuid.UUID, company_id: uuid.UUID) -> List[Notification]:
        notifications = self.db.query(NotificationModel).filter(
            NotificationModel.client_id == client_id,
            NotificationModel.company_id == company_id
        ).order_by(NotificationModel.created_at.desc()).all()

        return [self._to_entity(n) for n in notifications]

    # GET BY CHARGE
    def get_by_charge(self, charge_id: uuid.UUID, company_id: uuid.UUID) -> List[Notification]:
        notifications = self.db.query(NotificationModel).filter(
            NotificationModel.charge_id == charge_id,
            NotificationModel.company_id == company_id
        ).order_by(NotificationModel.created_at.desc()).all()

        return [self._to_entity(n) for n in notifications]

    # Mapper interno
    def _to_entity(self, model: NotificationModel) -> Notification:
        return Notification(
            id=model.id,
            company_id=model.company_id,
            client_id=model.client_id,
            user_id=model.user_id,
            charge_id=model.charge_id,
            type=model.type,
            message=model.message,
            channel=model.channel,
            status=model.status,
            sent_at=model.sent_at,
            created_at=model.created_at,
        )