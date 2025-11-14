from pydantic import BaseModel, Field
from pydantic import ConfigDict

# -------------------------- SCHEMA CREATE -------------------------------------
class TipoGastoCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description="Nome do Tipo de Gasto")


class TipoGastoCreateResponse(BaseModel):
    id: int
    nome: str
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'nome': 'Alimentação',
                'message': 'Tipo de Gasto criado com sucesso.'
            }
        }
    )


# # -------------------------- SCHEMA DELETE -------------------------------------
class TipoGastoDeleteResponse(BaseModel):
    nome: str
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'nome': 'Alimentação',
                'message': 'Tipo de Gasto excluído com sucesso.'
            }
        }
    )


# -------------------------- SCHEMA EDIT -------------------------------------
class TipoGastoEdit(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description='Nome do Tipo Gasto')


class TipoGastoEditResponse(BaseModel):
    nome: str
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'nome': 'Alimentação',
                'message': 'Tipo de Gasto editado com sucesso.'
            }
        }
    )


# -------------------------- SCHEMA LIST -------------------------------------

class TipoGastoListResponse(BaseModel):
    id: int
    nome: str

# -------------------------- SCHEMA VIEW -------------------------------------

class TipoGastoViewResponse(BaseModel):
    id: int
    nome: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'nome': 'Alimentação',
                'message': 'Dados retornados com sucesso.'
            }
        }
    )
