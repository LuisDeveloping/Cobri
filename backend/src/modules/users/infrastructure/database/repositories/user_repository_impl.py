# USERS REPOSITORY IMPLEMENTATION

from typing import Optional, List
import uuid

from sqlalchemy.orm import Session

from src.core.database.base_repository import BaseRepository
from src.modules.users.domain.interfaces.user_repository import UserRepository
from src.modules.users.domain.entities.user_entity import User
from src.modules.users.infrastructure.database.models.user_model import UserModel


class SqlAlchemyUserRepository(BaseRepository, UserRepository):

    def __init__(self, db: Session):
        super().__init__(db, UserModel)

    # CREATE USER
    def create(self, user: User) -> User:
        user_model = UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password_hash=user.password_hash,
            role=user.role,
            company_id=user.company_id,
            status=user.status,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

        saved_user = super().create(user_model)

        return self._to_entity(saved_user)

    # GET USER BY ID
    def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        user_model = super().get_by_id(user_id)

        if not user_model:
            return None

        return self._to_entity(user_model)

    # GET USER BY EMAIL
    def get_by_email(self, email: str) -> Optional[User]:
        user_model = (
            self.db.query(UserModel)
            .filter(UserModel.email == email)
            .first()
        )

        if not user_model:
            return None

        return self._to_entity(user_model)

    # GET ALL USERS
    def get_all(self) -> List[User]:
        users = self.db.query(UserModel).filter(
            UserModel.status == "active"
        ).all()

        return [self._to_entity(user) for user in users]

    # UPDATE USER
    def update(self, user: User) -> User:
        user_model = self.db.query(UserModel).filter(
            UserModel.id == user.id
        ).first()

        if not user_model:
            return None

        user_model.name = user.name
        user_model.email = user.email
        user_model.password_hash = user.password_hash
        user_model.role = user.role
        user_model.status = user.status
        user_model.updated_at = user.updated_at

        self.db.commit()
        self.db.refresh(user_model)

        return self._to_entity(user_model)

    # DELETE USER
    def delete(self, user_id: uuid.UUID) -> None:
        user_model = self.db.query(UserModel).filter(
            UserModel.id == user_id
        ).first()

        if not user_model:
            return None

        user_model.status = "inactive"

        self.db.commit()
    
    # GET ONLY BY COMPANY ID
    def get_by_company(self, company_id):
        users = self.db.query(UserModel).filter(
            UserModel.company_id == company_id,
            UserModel.status == "active"
        ).all()

        return [
            User(
                id=user.id,
                name=user.name,
                email=user.email,
                password_hash=user.password_hash,
                role=user.role,
                company_id=user.company_id,
                status=user.status,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users
        ]

    # Mapper interno (MUY IMPORTANTE)
    def _to_entity(self, user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            password_hash=user_model.password_hash,
            role=user_model.role,
            company_id=user_model.company_id,
            status=user_model.status,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
        )