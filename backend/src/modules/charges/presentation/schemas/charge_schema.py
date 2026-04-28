# CHARGES SCHEMAS

from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime
from decimal import Decimal

# CREATE CHARGE REQUEST
class CreateChargeRequest(BaseModel):
    client_id: uuid.UUID
    amount: Decimal
    description: str
    charge_date: datetime
    due_date: Optional[datetime] = None

# UPDATE CHARGE REQUEST
class UpdateChargeRequest(BaseModel):
    description: str
    due_date: Optional[datetime] = None

# FILTER CHARGES REQUEST (Query Params)
class FilterChargesRequest(BaseModel):
    status: Optional[str] = None
    client_id: Optional[uuid.UUID] = None
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None

# CHARGE RESPONSE
class ChargeResponse(BaseModel):
    id: uuid.UUID
    company_id: uuid.UUID
    client_id: uuid.UUID
    amount: Decimal
    description: str
    charge_date: datetime
    due_date: Optional[datetime]
    status: str
    paid_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True