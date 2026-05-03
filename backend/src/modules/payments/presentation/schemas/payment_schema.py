# PAYMENTS SCHEMAS

from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime


# CREATE PAYMENT REQUEST
class CreatePaymentRequest(BaseModel):
    charge_id: uuid.UUID
    amount: float = Field(gt=0)
    payment_method: str
    paid_at: datetime
    reference: Optional[str] = None


# VOID PAYMENT REQUEST
class VoidPaymentRequest(BaseModel):
    reason: str


# PAYMENT RESPONSE
class PaymentResponse(BaseModel):
    id: uuid.UUID
    charge_id: uuid.UUID
    company_id: uuid.UUID
    amount: float
    payment_method: str
    reference: Optional[str]
    status: str
    paid_at: datetime
    voided_at: Optional[datetime]
    void_reason: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True