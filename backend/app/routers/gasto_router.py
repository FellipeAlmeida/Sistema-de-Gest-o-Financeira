from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from  database import get_db
from  models.tipo_receita_model import TipoReceita
from  schemas.tipo_receita_schema import TipoReceitaCreateResponse, TipoReceitaCreate

from  schemas.tipo_receita_schema import TipoReceitaDeleteResponse, TipoReceitaEditResponse, TipoReceitaEdit, \
    TipoReceitaListResponse, TipoReceitaViewResponse

from models.receita_model import Receita
from schemas.receita_schema import ReceitaCreateResponse, ReceitaDeleteResponse, ReceitaEditResponse, \
    ReceitaViewResponse, ReceitaListResponse

from  schemas.receita_schema import ReceitaCreate, ReceitaEdit

from  models.gasto_model import Gastos
from  schemas.gasto_schema import GastoCreateResponse, GastoCreate, GastoDeleteResponse, GastoEditResponse, \
    GastoListResponse, GastoViewResponse, GastoEdit
from  schemas.tipo_gasto_schema import TipoGastoCreateResponse

from models.tipo_gasto_model import TipoGasto

router = APIRouter(
    prefix="/Gasto",
    tags=["04. Gasto"]
)

# -------------------------- CREATE -------------------------------------

@router.post("", response_model=GastoCreateResponse)
def criar_gasto(gasto: GastoCreate, db: Session = Depends(get_db)):
    try:
        model = Gastos(**gasto.model_dump()) # model_dump transforma os dados em dicionário python para o sqlalchemy
        db.add(model)
        db.commit()
        db.refresh(model)

        return GastoCreateResponse(
            id=model.id,
            nome=model.nome,
            message="Gasto criado com sucesso!")
    except Exception as err:
        print(err)


# -------------------------- DELETE -------------------------------------

@router.delete("/{gasto_id}", response_model=GastoDeleteResponse)
def delete_gasto(gasto_id: int, db: Session = Depends(get_db)):
        model = db.query(Gastos).filter(Gastos.id == gasto_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Gasto não encontrado.")

        db.delete(model)
        db.commit()
        return GastoDeleteResponse(
            nome=model.nome,
            message="Gasto excluido com sucesso!"
        )

# -------------------------- EDIT -------------------------------------

@router.put("/{gasto_id}", response_model=GastoEditResponse)
def edit_gasto(gasto_id: int, gasto: GastoEdit, db: Session = Depends(get_db)):
        model = db.query(Gastos).filter(Gastos.id == gasto_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Gasto não encontrada.")

        for key, value in gasto.model_dump(exclude_unset=True).items():
            setattr(model, key, value)

        db.commit()
        return GastoEditResponse(
            nome=model.nome,
            tipo_gasto_id=model.tipo_gasto_id,
            valor=model.valor,
            data=model.data,
            descricao=model.descricao,
            eh_fixo=model.eh_fixo,
            message="Gasto atualizada com sucesso!"
        )

# -------------------------- LIST -------------------------------------

@router.get("/list/{gasto_id}", response_model=List[GastoListResponse])
def list_gasto(db: Session = Depends(get_db)):
    gastos = db.query(Gastos).all()
    return gastos

# -------------------------- VIEW -------------------------------------

@router.get("/{tipo_gasto_id}", response_model=GastoViewResponse)
def get_gasto(tipo_gasto_id: int, db: Session = Depends(get_db)):
        model = db.query(Gastos).join(TipoGasto).filter(TipoGasto.id == tipo_gasto_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Gasto não encontrado.")

        return GastoViewResponse(
            id=model.id,
            nome=model.nome,
            tipo_gasto_id=model.tipo_gasto_id,
            valor=model.valor,
            data=model.data,
            descricao=model.descricao,
            eh_fixo=model.eh_fixo
        )
