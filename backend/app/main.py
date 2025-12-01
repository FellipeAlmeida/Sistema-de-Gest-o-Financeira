from fastapi import FastAPI
from routers import tipo_gasto_router
from database import Base, engine
from routers import tipo_receita_router
from routers import receita_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import gasto_router

# cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestão Financeira")

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "*"  # se quiser liberar geral (temporário)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tipo_gasto_router.router)
app.include_router(tipo_receita_router.router)
app.include_router(receita_router.router)
app.include_router(gasto_router.router)


@app.get("/")
def teste():
    return {"msg": "teste"}