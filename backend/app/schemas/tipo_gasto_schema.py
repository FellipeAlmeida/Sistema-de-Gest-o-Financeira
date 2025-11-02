from pydantic import BaseModel, Field

class TipoGastoResponse(BaseModel):
    id: int
    nome: str

class TipoGastoCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description="Nome do Tipo de Gasto")

class TipoGastoCreateResponse(BaseModel):
    id: int
    message: str = "Tipo de Gasto criado com sucesso!"