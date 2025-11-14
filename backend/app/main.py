from fastapi import FastAPI
from app.routers import tipo_gasto_router
from app.database import Base, engine
from app.routers import tipo_receita_router

# cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestão Financeira")

app.include_router(tipo_gasto_router.router)
app.include_router(tipo_receita_router.router)


@app.get("/")
def teste():
    return {"msg": "teste"}