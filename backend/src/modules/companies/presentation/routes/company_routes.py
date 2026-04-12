# COMPANIES ROUTE
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from src.core.dependecies.company_dependencies import get_company_repository
from src.modules.companies.domain.interfaces.company_repository import CompanyRepository
from src.modules.companies.presentation.schemas.company_schema import (CreateCompanyRequest,CompanyResponse,UpdateCompanyRequest)
from src.modules.companies.application.use_cases.commands.company_command import create_company
from src.modules.companies.application.use_cases.commands.company_command import update_company
from src.modules.companies.application.use_cases.commands.company_command import delete_company
from src.modules.companies.application.use_cases.queries.company_query import get_company_by_id
from src.modules.companies.application.use_cases.queries.company_query import get_all_companies


router = APIRouter(prefix="/companies", tags=["Companies"])

# POST/companies/Create Company Route
@router.post("/", response_model=CompanyResponse)
def create_company_route(
    request: CreateCompanyRequest,
    repository: CompanyRepository = Depends(get_company_repository),
):
    try:
        company = create_company(
            repository=repository,
            name=request.name,
            email=request.email,
            tax_id=request.tax_id,
            phone=request.phone,
        )

        return company

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# GET/companies/{company_id}/Get Company By Id Route
@router.get("/{company_id}", response_model=CompanyResponse)
def get_company_by_id_route(
    company_id: str,
    repository: CompanyRepository = Depends(get_company_repository),
):
    try:
        company = get_company_by_id(
            repository=repository,
            company_id=company_id,
        )
        return company

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# GET/companies/Get All Companies Route
@router.get("/", response_model=List[CompanyResponse])
def get_all_companies_route(
    repository: CompanyRepository = Depends(get_company_repository),
):
    companies = get_all_companies(repository=repository)
    return companies

@router.put("/{company_id}", response_model=CompanyResponse)
def update_company_route(
    company_id: str,
    request: UpdateCompanyRequest,
    repository: CompanyRepository = Depends(get_company_repository),
):
    try:
        company = update_company(
            repository=repository,
            company_id=company_id,
            name=request.name,
            email=request.email,
            tax_id=request.tax_id,
            phone=request.phone,
        )
        return company

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company_route(
    company_id: str,
    repository: CompanyRepository = Depends(get_company_repository),
):
    try:
        delete_company(
            repository=repository,
            company_id=company_id,
        )
        return

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))