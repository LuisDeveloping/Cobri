# LOGIN USER USE CASE

from src.modules.users.domain.interfaces.user_repository import UserRepository
from src.modules.auth.infrastructure.database.models.refresh_token_model import RefreshTokenModel

from src.core.security.password import verify_password
from src.core.security.jwt_handler import create_access_token
from src.core.security.jwt_handler import create_access_token, create_refresh_token

from datetime import datetime, timedelta

def login_user(
    repository: UserRepository,
    email: str,
    password: str,
    db
):
    # Buscar usuario
    user = repository.get_by_email(email)

    if not user:
        raise ValueError("Credenciales inválidas")

    # Verificar estado
    if user.status != "active":
        raise ValueError("Usuario inactivo")

    # Verificar password
    if not verify_password(password, user.password_hash):
        raise ValueError("Credenciales inválidas")

    # Access token
    access_token = create_access_token({
        "sub": str(user.id),
        "company_id": str(user.company_id),
        "role": user.role,
    })

    # Refresh token
    refresh_token = create_refresh_token({
        "sub": str(user.id)
    })

    # Guardar en DB
    db_token = RefreshTokenModel(
        user_id=user.id,
        token=refresh_token,
        expires_at=datetime.utcnow() + timedelta(days=7)
    )

    db.add(db_token)
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }