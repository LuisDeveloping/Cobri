# COMPANIES COMMAND
from datetime import datetime
from src.modules.companies.domain.entities.company_entity import Company
from src.modules.companies.domain.interfaces.company_repository import CompanyRepository

# CREATE COMPANY COMMAND
def create_company(
    repository: CompanyRepository,
    name: str,
    email: str,
    tax_id: str,
    phone: str | None = None,
):
    # 1. Validar si ya existe
    existing_company = repository.get_by_email(email)

    if existing_company:
        raise ValueError("El email ya está registrado")

    # 2. Crear entidad de dominio
    company = Company(
        name=name,
        email=email,
        tax_id=tax_id,
        phone=phone,
    )

    # 3. Guardar usando repository
    return repository.create(company)

# UPDATE COMPANY COMMAND
def update_company(
    repository: CompanyRepository,
    company_id: str,
    name: str,
    email: str,
    tax_id: str,
    phone: str | None,
) -> Company:

    company = repository.get_by_id(company_id)

    if not company:
        raise ValueError("Empresa no encontrada")

    # Validar email duplicado (si cambia)
    existing = repository.get_by_email(email)
    if existing and str(existing.id) != str(company_id):
        raise ValueError("El email ya está registrado")

    # Aquí podriamos validar tax_id también luego

    # Actualizar campos
    company.name = name
    company.email = email
    company.tax_id = tax_id
    company.phone = phone
    company.updated_at = datetime.utcnow()

    return repository.update(company)

# DELETE COMPANY COMMAND
def delete_company(
    repository: CompanyRepository,
    company_id: str,
) -> None:

    company = repository.get_by_id(company_id)

    if not company:
        raise ValueError("Empresa no encontrada")

    company.status = "inactive"
    company.updated_at = datetime.utcnow()

    repository.update(company)