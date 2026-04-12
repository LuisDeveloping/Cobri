from typing import Optional, List
from sqlalchemy.orm import Session

from src.core.database.base_repository import BaseRepository
from src.modules.companies.domain.interfaces.company_repository import CompanyRepository
from src.modules.companies.domain.entities.company_entity import Company
from src.modules.companies.infrastructure.database.models.company_model import CompanyModel


class SqlAlchemyCompanyRepository(BaseRepository, CompanyRepository):

    def __init__(self, db: Session):
        super().__init__(db, CompanyModel)

    # CREATE COMPANY
    def create(self, company: Company) -> Company:
        company_model = CompanyModel(
            id=company.id,
            name=company.name,
            email=company.email,
            phone=company.phone,
            tax_id=company.tax_id,
            status=company.status,
            plan=company.plan,
            created_at=company.created_at,
            updated_at=company.updated_at,
        )

        saved_company = super().create(company_model)

        return Company(
            id=saved_company.id,
            name=saved_company.name,
            email=saved_company.email,
            phone=saved_company.phone,
            tax_id=saved_company.tax_id,
            status=saved_company.status,
            plan=saved_company.plan,
            created_at=saved_company.created_at,
            updated_at=saved_company.updated_at,
        )
    
    # UPDATE COMPANY
    def update(self, company: Company) -> Company:
        company_model = self.db.query(CompanyModel).filter(
        CompanyModel.id == company.id
        ).first()

        if not company_model:
            return None

        company_model.name = company.name
        company_model.email = company.email
        company_model.tax_id = company.tax_id
        company_model.phone = company.phone
        company_model.status = company.status
        company_model.updated_at = company.updated_at

        self.db.commit()
        self.db.refresh(company_model)

        return Company(
            id=company_model.id,
            name=company_model.name,
            email=company_model.email,
            phone=company_model.phone,
            tax_id=company_model.tax_id,
            status=company_model.status,
            plan=company_model.plan,
            created_at=company_model.created_at,
            updated_at=company_model.updated_at,
        )

    # GET EMAIL
    def get_by_email(self, email: str) -> Optional[Company]:
        company_model = (
            self.db.query(CompanyModel)
            .filter(CompanyModel.email == email)
            .first()
        )

        if not company_model:
            return None

        return Company(
            id=company_model.id,
            name=company_model.name,
            email=company_model.email,
            phone=company_model.phone,
            tax_id=company_model.tax_id,
            status=company_model.status,
            plan=company_model.plan,
            created_at=company_model.created_at,
            updated_at=company_model.updated_at,
        )
    
    # GET COMPANY BY ID
    def get_by_id(self, company_id: str) -> Optional[Company]:
        company_model = self.db.query(CompanyModel).filter(
            CompanyModel.id == company_id
        ).first()

        if not company_model:
            return None

        return Company(
            id=company_model.id,
            name=company_model.name,
            email=company_model.email,
            phone=company_model.phone,
            tax_id=company_model.tax_id,
            status=company_model.status,
            plan=company_model.plan,
            created_at=company_model.created_at,
            updated_at=company_model.updated_at,
        )
    
    # GET ALL COMPANIES
    def get_all(self) -> List[Company]:
        companies = self.db.query(CompanyModel).filter(
            CompanyModel.status == "active"
        ).all()

        return [
            Company(
                id=company.id,
                name=company.name,
                email=company.email,
                phone=company.phone,
                tax_id=company.tax_id,
                status=company.status,
                plan=company.plan,
                created_at=company.created_at,
                updated_at=company.updated_at,
            )
            for company in companies
        ]