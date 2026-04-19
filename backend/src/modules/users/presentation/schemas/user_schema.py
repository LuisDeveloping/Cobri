# USERS SCHEMAS

from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
from datetime import datetime


# CREATE USER REQUEST
class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str
    company_id: uuid.UUID


# UPDATE USER REQUEST
class UpdateUserRequest(BaseModel):
    name: str
    email: EmailStr
    role: str


# USER RESPONSE
class UserResponse(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    role: str
    company_id: uuid.UUID
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # importante para ORM

# LOGIN REQUEST
class LoginUserRequest(BaseModel):
    email: EmailStr
    password: str

# TOKEN RESPONSE
class TokenResponse(BaseModel):
    access_token: str
    token_type: str