from pydantic import BaseModel, Field
from pydantic import ConfigDict

# -------------------------- SCHEMA CREATE -------------------------------------
class TipoReceitaCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description="Nome do Tipo de Receita")

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'nome': 'Emprego',
                'message': 'Tipo de Receita criado com sucesso.'
            }
        }
    )

class TipoReceitaCreateResponse(BaseModel):
    id: int
    nome: str
    message: str

# # -------------------------- SCHEMA DELETE -------------------------------------
class TipoReceitaDeleteResponse(BaseModel):
    nome: str
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'nome': 'Emprego',
                'message': 'Tipo de Receita excluído com sucesso.'
            }
        }
    )


# -------------------------- SCHEMA EDIT -------------------------------------
class TipoReceitaEdit(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description='Nome do Tipo de Receita')


class TipoReceitaEditResponse(BaseModel):
    nome: str
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'nome': 'Emprego',
                'message': 'Tipo de Receita editado com sucesso.'
            }
        }
    )


# -------------------------- SCHEMA LIST -------------------------------------

class TipoReceitaListResponse(BaseModel):
    id: int
    nome: str

# -------------------------- SCHEMA VIEW -------------------------------------

class TipoReceitaViewResponse(BaseModel):
    id: int
    nome: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'nome': 'Emprego',
            }
        }
    )
