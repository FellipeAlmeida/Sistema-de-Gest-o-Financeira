from pydantic import BaseModel, Field
from pydantic import ConfigDict
from datetime import date

# -------------------------- SCHEMA CREATE -------------------------------------
class ReceitaCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description="Nome da Receita")
    valor: int = Field(description='Valor Recebido')
    data: date = Field(description='Data da Transação')
    descricao: str = Field(description='Descrição da Receita')
    eh_fixo: bool = Field(description='Define se a Receita é fixa')

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'nome': 'Salário',
                'valor': 1500,
                'data': '2024-02-04',
                'descricao': 'Salário do meu emprego',
                'eh_fixo': True,
                'message': 'Receita criada com sucesso.'
            }
        }
    )


class ReceitaCreateResponse(BaseModel):
    id: int
    nome: str
    message: str

# # -------------------------- SCHEMA DELETE -------------------------------------
class ReceitaDeleteResponse(BaseModel):
    nome: str
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'nome': 'Salário',
                'message': 'Receita excluída com sucesso.'
            }
        }
    )


# -------------------------- SCHEMA EDIT -------------------------------------
class ReceitaEdit(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description='Nome da Receita')
    valor: int = Field(description='Valor Recebido')
    data: date = Field(description='Data da Transação')
    descricao: str = Field(description='Descrição da Receita')
    eh_fixo: bool = Field(description='Define se a Receita é fixa')

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'nome': 'Salário',
                'valor': 1500,
                'data': '2024-02-04',
                'descricao': 'Salário do meu emprego',
                'eh_fixo': True,
            }
        }
    )

class ReceitaEditResponse(BaseModel):
    nome: str
    nome: str
    valor: int
    data: date
    descricao: str
    eh_fixo: bool
    message: str

# -------------------------- SCHEMA LIST -------------------------------------

class ReceitaListResponse(BaseModel):
    id: int
    nome: str
    valor: int = Field(description='Valor Recebido')
    data: date = Field(description='Data da Transação')
    descricao: str = Field(description='Descrição da Receita')
    eh_fixo: bool = Field(description='Define se a Receita é fixa')

# -------------------------- SCHEMA VIEW -------------------------------------

class ReceitaViewResponse(BaseModel):
    id: int
    nome: str
    valor: int = Field(description='Valor Recebido')
    data: date = Field(description='Data da Transação')
    descricao: str = Field(description='Descrição da Receita')
    eh_fixo: bool = Field(description='Define se a Receita é fixa')

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'nome': 'Salário',
                'valor': 1500,
                'data': '2024-02-04',
                'descricao': 'Salário do meu emprego',
                'eh_fixo': True,
                'message': 'Receita editada com sucesso.'
            }
        }
    )
