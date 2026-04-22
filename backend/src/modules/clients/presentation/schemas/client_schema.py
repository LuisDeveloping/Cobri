# CLIENTS SCHEMAS

from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
from datetime import datetime

class CreateClientRequest(BaseModel):
    name: str
    phone: str
    email: Optional[EmailStr] = None
    identification: Optional[str] = None
    notes: Optional[str] = None

class UpdateClientRequest(BaseModel):
    name: str
    phone: str
    email: Optional[EmailStr] = None
    identification: Optional[str] = None
    notes: Optional[str] = None

class ClientResponse(BaseModel):
    id: uuid.UUID
    name: str
    phone: str
    email: Optional[EmailStr]
    identification: Optional[str]
    notes: Optional[str]
    company_id: uuid.UUID
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True