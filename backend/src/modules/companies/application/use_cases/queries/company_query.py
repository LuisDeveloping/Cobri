# COMPANIES QUERIES
from typing import List

from src.modules.companies.domain.interfaces.company_repository import CompanyRepository
from src.modules.companies.domain.entities.company_entity import Company

# Get company by id query
def get_company_by_id(
    repository: CompanyRepository,
    company_id: str,
) -> Company:
    
    company = repository.get_by_id(company_id)

    if not company:
        raise ValueError("Empresa no encontrada")

    return company

# Get all companies query
def get_all_companies(
    repository: CompanyRepository,
) -> List[Company]:
    
    companies = repository.get_all()
    
    return companies