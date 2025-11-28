from pydantic import BaseModel, Field
from pydantic import ConfigDict
from datetime import date

# -------------------------- SCHEMA CREATE -------------------------------------
class GastoCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description="Nome do Gasto")
    tipo_gasto_id: int =  Field(description="Identificador de Tipo de Gasto")
    valor: int = Field(description='Valor Gasto')
    data: date = Field(description='Data da Transação')
    descricao: str = Field(description='Descrição do Gasto')
    eh_fixo: bool = Field(description='Define se o Gasto é fixo')

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'nome': 'Transporte',
                'tipo_gasto_id': 1,
                'valor': 300,
                'data': '2024-02-04',
                'descricao': 'Transporte até o meu emprego',
                'eh_fixo': True,
            }
        }
    )


class GastoCreateResponse(BaseModel):
    id: int
    nome: str
    message: str

# # -------------------------- SCHEMA DELETE -------------------------------------
class GastoDeleteResponse(BaseModel):
    nome: str
    message: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'nome': 'Transporte',
                'message': 'Gasto excluído com sucesso.'
            }
        }
    )


# -------------------------- SCHEMA EDIT -------------------------------------
class GastoEdit(BaseModel):
    nome: str = Field(min_length=3, max_length=100, description="Nome do Gasto")
    tipo_gasto_id: int = Field(description="Identificador de Tipo de Gasto")
    valor: int = Field(description='Valor Gasto')
    data: date = Field(description='Data da Transação')
    descricao: str = Field(description='Descrição do Gasto')
    eh_fixo: bool = Field(description='Define se o Gasto é fixo')

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'nome': 'Transporte',
                'tipo_gasto_id': 1,
                'valor': 300,
                'data': '2024-02-04',
                'descricao': 'Transporte até o meu emprego',
                'eh_fixo': True,
            }
        }
    )

class GastoEditResponse(BaseModel):
    nome: str
    tipo_gasto_id: int
    valor: int
    data: date
    descricao: str
    eh_fixo: bool
    message: str

# -------------------------- SCHEMA LIST -------------------------------------

class GastoListResponse(BaseModel):
    id: int
    nome: str
    tipo_gasto_id: int
    valor: int
    data: date
    descricao: str
    eh_fixo: bool

# -------------------------- SCHEMA VIEW -------------------------------------

class GastoViewResponse(BaseModel):
    id: int
    nome: str
    tipo_gasto_id: int
    valor: int
    data: date
    descricao: str
    eh_fixo: bool

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'nome': 'Transporte',
                'tipo_gasto_id': 1,
                'valor': 300,
                'data': '2024-02-04',
                'descricao': 'Transporte até o meu emprego',
                'eh_fixo': True,
            }
        }
    )
