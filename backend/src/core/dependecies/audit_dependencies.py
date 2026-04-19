from src.modules.audit.infrastructure.database.repository.audit_log_repository import AuditLogRepository
from src.core.database.session import get_db
from fastapi import Depends


def get_audit_repository(db = Depends(get_db)):
    return AuditLogRepository(db)