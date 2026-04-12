# COMPANIES REPOSITORY (Interface)
from abc import ABC, abstractmethod
from typing import Optional, List

from src.modules.companies.domain.entities.company_entity import Company

class CompanyRepository(ABC):

    @abstractmethod
    def create(self, company: Company) -> Company:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[Company]:
        pass

    @abstractmethod
    def get_by_id(self, company_id: str) -> Optional[Company]:
        pass

    @abstractmethod
    def get_all(self) -> List[Company]:
        pass

    @abstractmethod
    def update(self, company: Company) -> Company:
        pass