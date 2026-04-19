# REPOSITORY LOGS

from sqlalchemy.orm import Session
from src.modules.audit.infrastructure.database.models.audit_log_model import AuditLogModel


class AuditLogRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_log(self, user_id, action, entity, entity_id):
        log = AuditLogModel(
            user_id=user_id,
            action=action,
            entity=entity,
            entity_id=entity_id,
        )

        self.db.add(log)
        self.db.commit()