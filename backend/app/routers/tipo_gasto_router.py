from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.tipo_gasto_model import TipoGasto
from schemas.tipo_gasto_schema import TipoGastoCreate, TipoGastoCreateResponse
from database import get_db
from schemas.tipo_gasto_schema import TipoGastoDeleteResponse
from schemas.tipo_gasto_schema import TipoGastoEditResponse
from schemas.tipo_gasto_schema import TipoGastoEdit
from schemas.tipo_gasto_schema import TipoGastoViewResponse
from schemas.tipo_gasto_schema import TipoGastoListResponse

router = APIRouter(
    prefix="/tipo_gasto",
    tags=["01. Tipo Gasto"]
)

# -------------------------- CREATE -------------------------------------

@router.post("", response_model=TipoGastoCreateResponse)
def criar_tipo_gasto(tipo_gasto: TipoGastoCreate, db: Session = Depends(get_db)):
        model = TipoGasto(**tipo_gasto.model_dump()) # model_dump transforma os dados em dicionário python para o sqlalchemy
        db.add(model)
        db.commit()
        db.refresh(model)

        return TipoGastoCreateResponse(
            id=model.id,
            nome=model.nome,
            message="Tipo de Gasto criado com sucesso!")


# -------------------------- DELETE -------------------------------------

@router.delete("/{tipo_gasto_id}", response_model=TipoGastoDeleteResponse)
def delete_tipo_gasto(tipo_gasto_id: int, db: Session = Depends(get_db)):
        model = db.query(TipoGasto).filter(TipoGasto.id == tipo_gasto_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Tipo de Gasto não encontrado.")

        db.delete(model)
        db.commit()
        return TipoGastoDeleteResponse(
            nome=model.nome,
            message="Tipo de Gasto excluido com sucesso!"
        )

# -------------------------- EDIT -------------------------------------

@router.put("/{tipo_gasto_id}", response_model=TipoGastoEditResponse)
def edit_tipo_gasto(tipo_gasto_id: int, tipo_gasto: TipoGastoEdit, db: Session = Depends(get_db)):
        model = db.query(TipoGasto).filter(TipoGasto.id == tipo_gasto_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Tipo de Gasto não encontrado.")

        for key, value in tipo_gasto.model_dump(exclude_unset=True).items():
            setattr(model, key, value)

        db.commit()
        return TipoGastoEditResponse(
            nome=model.nome,
            message="Tipo de Gasto atualizado com sucesso!"
        )

# -------------------------- LIST -------------------------------------

@router.get("/list", response_model=List[TipoGastoListResponse])
def list_tipo_gasto(db: Session = Depends(get_db)):
    tipos_gastos = db.query(TipoGasto).all()
    return tipos_gastos

# -------------------------- VIEW -------------------------------------

@router.get("/{tipo_gasto_id}", response_model=TipoGastoViewResponse)
def get_tipo_gasto(tipo_gasto_id: int, db: Session = Depends(get_db)):
        model = db.query(TipoGasto).filter(TipoGasto.id == tipo_gasto_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Tipo de Gasto não encontrado.")

        return TipoGastoViewResponse(
            id=model.id,
            nome=model.nome
        )
