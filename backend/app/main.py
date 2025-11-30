from fastapi import FastAPI
from routers import tipo_gasto_router
from database import Base, engine
from routers import tipo_receita_router
from routers import receita_router

from routers import gasto_router

# cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestão Financeira")

app.include_router(tipo_gasto_router.router)
app.include_router(tipo_receita_router.router)
app.include_router(receita_router.router)
app.include_router(gasto_router.router)


@app.get("/")
def teste():
    return {"msg": "teste"}