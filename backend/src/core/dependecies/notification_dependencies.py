from sqlalchemy.orm import Session
from fastapi import Depends

from src.core.database.session import get_db

from src.modules.notifications.domain.interfaces.notification_repository import NotificationRepository
from src.modules.notifications.infrastructure.database.repositories.notification_repository_impl import (
    SqlAlchemyNotificationRepository,
)


def get_notification_repository(db: Session = Depends(get_db)) -> NotificationRepository:
    return SqlAlchemyNotificationRepository(db)