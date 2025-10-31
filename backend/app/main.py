from fastapi import FastAPI

app = FastAPI(title="Sistema de Gestão Financeira")

@app.get("/")
def teste():
    return {"msg": "teste"}