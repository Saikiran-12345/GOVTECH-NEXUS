from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class PermissionRead(BaseModel):
    id: int
    name: str
    code: str
    resource: str
    action: str

    class Config:
        from_attributes = True

class RoleRead(BaseModel):
    id: int
    name: str
    code: str
    description: Optional[str] = None
    permissions: List[PermissionRead] = []

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    full_name: str
    phone_number: Optional[str] = None

class UserRead(BaseModel):
    id: int
    email: EmailStr
    username: str
    full_name: str
    phone_number: Optional[str] = None
    is_active: bool
    is_superuser: bool
    status: str
    roles: List[RoleRead] = []
    created_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    is_active: Optional[bool] = None
    status: Optional[str] = None

class LoginRequest(BaseModel):
    username_or_email: str
    password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserRead

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    type: Optional[str] = None

class PasswordChangeRequest(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=6)

class RoleAssignRequest(BaseModel):
    role_ids: List[int]
