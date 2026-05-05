# NOTIFICATION SCHEMAS

from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime


# RESPONSE
class NotificationResponse(BaseModel):
    id: uuid.UUID
    company_id: uuid.UUID
    client_id: Optional[uuid.UUID]
    user_id: Optional[uuid.UUID]
    charge_id: Optional[uuid.UUID]
    type: str
    message: str
    channel: str
    status: str
    sent_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True