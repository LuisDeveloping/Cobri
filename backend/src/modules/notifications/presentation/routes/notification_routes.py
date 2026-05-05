from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid

from src.core.dependecies.notification_dependencies import get_notification_repository
from src.core.dependecies.auth_dependencies import get_current_user

from src.modules.notifications.application.use_cases.queries.notification_query import (
    get_notifications,
    get_notification_by_id,
)

from src.modules.notifications.presentation.schemas.notification_schema import (
    NotificationResponse,
)

router = APIRouter(prefix="/notifications", tags=["Notifications"])


# GET /notifications/
@router.get("/", response_model=List[NotificationResponse])
def get_all_notifications_route(
    repository=Depends(get_notification_repository),
    current_user=Depends(get_current_user),
):
    return get_notifications(
        repository=repository,
        company_id=current_user.company_id,
    )


# GET /notifications/{notification_id}
@router.get("/{notification_id}", response_model=NotificationResponse)
def get_notification_by_id_route(
    notification_id: uuid.UUID,
    repository=Depends(get_notification_repository),
    current_user=Depends(get_current_user),
):
    notification = get_notification_by_id(
        repository=repository,
        notification_id=notification_id,
        company_id=current_user.company_id,
    )

    if not notification:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")

    return notification