# USERS COMMANDS

from datetime import datetime

from src.modules.users.domain.entities.user_entity import User
from src.modules.users.domain.interfaces.user_repository import UserRepository
from src.core.security.password import hash_password

# CREATE USER
def create_user(
    repository: UserRepository,
    name: str,
    email: str,
    password: str,
    role: str,
    company_id,
):
    # Validar si ya existe el usuario
    existing_user = repository.get_by_email(email)

    if existing_user:
        raise ValueError("El usuario ya existe con ese correo")
    
    # Hash password
    hashed_password = hash_password(password)

    # Crear entidad (aquí se ejecutan validaciones del dominio)
    user = User(
        name=name,
        email=email,
        password_hash = hashed_password,
        role=role,
        company_id=company_id,
    )

    # Guardar
    return repository.create(user)

# UPDATE USER
def update_user(
    repository: UserRepository,
    user_id: str,
    name: str,
    email: str,
    role: str,
):
    # Buscar usuario
    user = repository.get_by_id(user_id)

    if not user:
        raise ValueError("Usuario no encontrado")

    # Validar email duplicado (si cambió)
    existing_user = repository.get_by_email(email)

    if existing_user and existing_user.id != user.id:
        raise ValueError("El correo ya está en uso")

    # Actualizar datos
    user.name = name
    user.email = email

    # usar método de dominio
    user.change_role(role)

    user.updated_at = datetime.utcnow()

    # Guardar
    return repository.update(user)

# DELETE USER (SOFT DELETE)
def delete_user(repository: UserRepository, user_id: str,):
    # Buscar usuario
    user = repository.get_by_id(user_id)

    if not user:
        raise ValueError("Usuario no encontrado")

    # Lógica de dominio
    user.deactivate()

    # Guardar cambios
    repository.update(user)