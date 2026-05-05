# NOTIFICATION QUERIES

from typing import List, Optional
import uuid

from src.modules.notifications.domain.entities.notification_entity import Notification
from src.modules.notifications.domain.interfaces.notification_repository import NotificationRepository


# GET ALL / FILTERED NOTIFICATIONS
def get_notifications(
    repository: NotificationRepository,
    company_id: uuid.UUID,
    client_id: Optional[uuid.UUID] = None,
    charge_id: Optional[uuid.UUID] = None,
    status: Optional[str] = None,
) -> List[Notification]:

    # Base: todas por empresa
    notifications = repository.get_by_company(company_id)

    # Filtros en memoria
    if client_id:
        notifications = [n for n in notifications if n.client_id == client_id]

    if charge_id:
        notifications = [n for n in notifications if n.charge_id == charge_id]

    if status:
        notifications = [n for n in notifications if n.status == status]

    return notifications


def get_notification_by_id(
    repository: NotificationRepository,
    notification_id: uuid.UUID,
    company_id: uuid.UUID,
) -> Optional[Notification]:

    notification = repository.get_by_id(notification_id)

    if not notification or notification.company_id != company_id:
        return None

    return notification