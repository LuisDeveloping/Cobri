from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.database.session import get_db
from src.modules.companies.domain.interfaces.company_repository import CompanyRepository
from src.modules.companies.infrastructure.database.repositories.company_repository_impl import (
    SqlAlchemyCompanyRepository,
)


def get_company_repository(
    db: Session = Depends(get_db),
) -> CompanyRepository:
    return SqlAlchemyCompanyRepository(db)