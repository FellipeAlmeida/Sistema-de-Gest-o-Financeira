from pydantic import BaseModel, Field

class TipoGastoResponse(BaseModel): # <- BaseModel é a classe base para validação dos dados e a geração de docs
    id: int
    nome: str

# --------------------------------------------------------------

class TipoGastoCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description="Nome do Tipo de Gasto")

class TipoGastoCreateResponse(BaseModel):
    id: int
    message: str

# --------------------------------------------------------------

class TipoGastoDelete(BaseModel):
    id: int = Field(description="Identificador do Tipo de Gasto")

class TipoGastoDeleteResponse(BaseModel):
    id: int
    message: str

# --------------------------------------------------------------
