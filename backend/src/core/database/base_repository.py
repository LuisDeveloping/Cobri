from sqlalchemy.orm import Session
from typing import Type, List, Optional


class BaseRepository:
    def __init__(self, db: Session, model: Type):
        self.db = db
        self.model = model

    def create(self, instance):
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def get_by_id(self, id) -> Optional[object]:
        return (
            self.db.query(self.model)
            .filter(self.model.id == id)
            .first()
        )

    def get_all(self) -> List[object]:
        return self.db.query(self.model).all()

    def delete(self, instance) -> None:
        self.db.delete(instance)
        self.db.commit()