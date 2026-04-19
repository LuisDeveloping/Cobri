from fastapi import FastAPI
from src.core.config import settings
from src.core.database.session import engine
from src.core.database.session import engine
from src.core.database.session import Base
from src.modules.companies.infrastructure.database.models.company_model import CompanyModel
from src.modules.companies.presentation.routes.company_routes import router as company_router
from src.modules.users.presentation.routes.user_routes import router as user_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Cobri backend running"}

@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection:
            return {"message": "DB connected successfully"}
    except Exception as e:
        return {"error": str(e)}
    
@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

# Companies Routers
app.include_router(company_router)

# Users Routers
app.include_router(user_router)