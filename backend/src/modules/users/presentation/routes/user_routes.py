# USERS ROUTES

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.orm import Session

from src.core.dependecies.user_dependencies import get_user_repository
from src.core.dependecies.auth_dependencies import get_current_user
from src.core.dependecies.role_dependencies import require_roles
from src.core.dependecies.audit_dependencies import get_audit_repository
from src.core.database.session import get_db

from src.modules.users.application.use_cases.commands.user_command import (create_user, update_user, delete_user,)
from src.modules.users.application.use_cases.queries.user_query import (get_all_users, get_user_by_id,)
from src.modules.users.presentation.schemas.user_schema import (CreateUserRequest, UpdateUserRequest, UserResponse,)
from src.modules.users.application.use_cases.auth.login_User import login_user
from src.modules.users.presentation.schemas.user_schema import LoginUserRequest
from src.modules.users.presentation.schemas.user_schema import TokenResponse

router = APIRouter(prefix="/users", tags=["Users"])

# GET/users/Get All Users Route
@router.get("/", response_model=List[UserResponse])
def get_all_users_route(
    repository=Depends(get_user_repository),
    current_user = Depends(get_current_user),
):
    return get_all_users(repository=repository, company_id=current_user.company_id,)

# GET/users/{user_id}/Get User By Id Route
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id_route(
    user_id: str,
    repository=Depends(get_user_repository),
    current_user = Depends(get_current_user),
):
    user = get_user_by_id(repository=repository, user_id=user_id)

    if not user or user.company_id != current_user.company_id:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user

# POST/users/Create User Route
@router.post("/", response_model=UserResponse)
def create_user_route(
    request: CreateUserRequest,
    repository=Depends(get_user_repository),
    audit_repo=Depends(get_audit_repository),
    current_user = Depends(require_roles(["admin", "owner"])),
):
    try:
        user = create_user(
            repository=repository,
            name=request.name,
            email=request.email,
            password=request.password,
            role=request.role,
            company_id=current_user.company_id,
        )

        # AUDITORÍA
        audit_repo.create_log(
            user_id=current_user.id,
            action="CREATE",
            entity="User",
            entity_id=user.id,
        )

        return user

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# POST/users/login/Login User Route
@router.post("/login", response_model=TokenResponse)
def login_user_route(
    request: LoginUserRequest,
    repository=Depends(get_user_repository),
    db: Session = Depends(get_db),
):
    try:
        token = login_user(
            repository=repository,
            email=request.email,
            password=request.password,
            db=db,
        )
        return token

    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

# PUT/users/{user_id}/Update User Route
@router.put("/{user_id}", response_model=UserResponse)
def update_user_route(
    user_id: str,
    request: UpdateUserRequest,
    repository=Depends(get_user_repository),
    audit_repo=Depends(get_audit_repository),
    current_user = Depends(require_roles(["admin", "owner"])),
):
    try:
        existing_user = get_user_by_id(repository=repository, user_id=user_id)

        if not existing_user or existing_user.company_id != current_user.company_id:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        user = update_user(
            repository=repository,
            user_id=user_id,
            name=request.name,
            email=request.email,
            role=request.role,
        )

        # AUDITORÍA
        audit_repo.create_log(
            user_id=current_user.id,
            action="UPDATE",
            entity="User",
            entity_id=user.id,
        )
        
        return user

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# DELETE/users/{user_id}/Delete User Route
@router.delete("/{user_id}", status_code=204)
def delete_user_route(
    user_id: str,
    repository=Depends(get_user_repository),
    audit_repo=Depends(get_audit_repository),
    current_user = Depends(require_roles(["admin", "owner"])),  # Proteccion de cuales roles pueden eliminar
):
    try:
        user = get_user_by_id(repository=repository, user_id=user_id)

        if not user or user.company_id != current_user.company_id:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        delete_user(repository=repository, user_id=user_id)

        # AUDITORÍA
        audit_repo.create_log(
            user_id=current_user.id,
            action="DELETE",
            entity="User",
            entity_id=user_id,
        )

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

