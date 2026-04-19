# USERS QUERIES

from typing import List, Optional

from src.modules.users.domain.entities.user_entity import User
from src.modules.users.domain.interfaces.user_repository import UserRepository

# GET ALL USERS
def get_all_users(repository: UserRepository,company_id,):
    return repository.get_by_company(company_id)

# GET USERS BY ID
def get_user_by_id(repository: UserRepository, user_id: str) -> Optional[User]:
    return repository.get_by_id(user_id)