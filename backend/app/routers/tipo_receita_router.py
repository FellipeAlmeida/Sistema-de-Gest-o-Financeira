from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_receita_model import TipoReceita
from app.schemas.tipo_receita_schema import TipoReceitaCreateResponse, TipoReceitaCreate

from app.schemas.tipo_receita_schema import TipoReceitaDeleteResponse, TipoReceitaEditResponse, TipoReceitaEdit, \
    TipoReceitaListResponse, TipoReceitaViewResponse

router = APIRouter(
    prefix="/tipo_receita",
    tags=["02. Tipo Receita"]
)

# -------------------------- CREATE -------------------------------------

@router.post("", response_model=TipoReceitaCreateResponse)
def criar_tipo_receita(tipo_receita: TipoReceitaCreate, db: Session = Depends(get_db)):
        model = TipoReceita(**tipo_receita.model_dump()) # model_dump transforma os dados em dicionário python para o sqlalchemy
        db.add(model)
        db.commit()
        db.refresh(model)

        return TipoReceitaCreateResponse(
            id=model.id,
            nome=model.nome,
            message="Tipo de Receita criado com sucesso!")


# -------------------------- DELETE -------------------------------------

@router.delete("/{tipo_receita_id}", response_model=TipoReceitaDeleteResponse)
def delete_tipo_receita(tipo_receita_id: int, db: Session = Depends(get_db)):
        model = db.query(TipoReceita).filter(TipoReceita.id == tipo_receita_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Tipo de Gasto não encontrado.")

        db.delete(model)
        db.commit()
        return TipoReceitaDeleteResponse(
            nome=model.nome,
            message="Tipo de Receita excluido com sucesso!"
        )

# -------------------------- EDIT -------------------------------------

@router.put("/{tipo_receita_id}", response_model=TipoReceitaEditResponse)
def edit_tipo_receita(tipo_receita_id: int, tipo_gasto: TipoReceitaEdit, db: Session = Depends(get_db)):
        model = db.query(TipoReceita).filter(TipoReceita.id == tipo_receita_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Tipo de Gasto não encontrado.")

        for key, value in tipo_gasto.model_dump(exclude_unset=True).items():
            setattr(model, key, value)

        db.commit()
        return TipoReceitaEditResponse(
            nome=model.nome,
            message="Tipo de Receita atualizado com sucesso!"
        )

# -------------------------- LIST -------------------------------------

@router.get("/list/{tipo_gasto_id}", response_model=List[TipoReceitaListResponse])
def list_tipo_receita(db: Session = Depends(get_db)):
    tipos_gastos = db.query(TipoReceita).all()
    return tipos_gastos

# -------------------------- VIEW -------------------------------------

@router.get("/{tipo_gasto_id}", response_model=TipoReceitaViewResponse)
def get_tipo_receita(tipo_receita_id: int, db: Session = Depends(get_db)):
        model = db.query(TipoReceita).filter(TipoReceita.id == tipo_receita_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Tipo de Gasto não encontrado.")

        return TipoReceitaViewResponse(
            id=model.id,
            nome=model.nome
        )
