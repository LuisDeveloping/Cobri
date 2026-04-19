# ROUTES AUTH

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from src.core.database.session import get_db
from src.core.security.jwt_handler import create_access_token, verify_token

from src.modules.auth.infrastructure.database.models.refresh_token_model import RefreshTokenModel
from src.modules.auth.presentation.schemas.refresh_schema import RefreshTokenRequest

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/refresh")
def refresh_token(
    request: RefreshTokenRequest,
    db: Session = Depends(get_db),
):
    payload = verify_token(request.refresh_token)

    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")

    db_token = db.query(RefreshTokenModel).filter(
        RefreshTokenModel.token == refresh_token
    ).first()

    if not db_token:
        raise HTTPException(status_code=401, detail="Token no reconocido")

    if db_token.expires_at < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Token expirado")

    # 🔥 Nuevo access token
    new_access_token = create_access_token({
        "sub": payload["sub"]
    })

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }