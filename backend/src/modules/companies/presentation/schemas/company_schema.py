# COMPANIES SCHEMA
from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

# CREATE COMPANY
class CreateCompanyRequest(BaseModel):
    name: str
    email: EmailStr
    tax_id: str
    phone: Optional[str] = None


class CompanyResponse(BaseModel):
    id: UUID
    name: str
    email: str
    phone: Optional[str]
    tax_id: str
    status: str
    plan: str

    class Config:
        from_attributes = True

# UPDATE COMPANY
class UpdateCompanyRequest(BaseModel):
    name: str
    email: EmailStr
    tax_id: str
    phone: Optional[str] = None