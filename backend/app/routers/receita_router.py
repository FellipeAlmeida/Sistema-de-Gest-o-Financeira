from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_receita_model import TipoReceita
from app.schemas.tipo_receita_schema import TipoReceitaCreateResponse, TipoReceitaCreate

from app.schemas.tipo_receita_schema import TipoReceitaDeleteResponse, TipoReceitaEditResponse, TipoReceitaEdit, \
    TipoReceitaListResponse, TipoReceitaViewResponse

from app.models.receita_model import Receita
from app.schemas.receita_schema import ReceitaCreateResponse, ReceitaDeleteResponse, ReceitaEditResponse, \
    ReceitaViewResponse, ReceitaListResponse

from app.schemas.receita_schema import ReceitaCreate, ReceitaEdit

router = APIRouter(
    prefix="/receita",
    tags=["03. Receita"]
)

# -------------------------- CREATE -------------------------------------

@router.post("", response_model=ReceitaCreateResponse)
def criar_receita(receita: ReceitaCreate, db: Session = Depends(get_db)):
        model = Receita(**receita.model_dump()) # model_dump transforma os dados em dicionário python para o sqlalchemy
        db.add(model)
        db.commit()
        db.refresh(model)

        return TipoReceitaCreateResponse(
            id=model.id,
            nome=model.nome,
            message="Receita criado com sucesso!")


# -------------------------- DELETE -------------------------------------

@router.delete("/{receita_id}", response_model=ReceitaDeleteResponse)
def delete_receita(receita_id: int, db: Session = Depends(get_db)):
        model = db.query(Receita).filter(Receita.id == receita_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Receita não encontrado.")

        db.delete(model)
        db.commit()
        return ReceitaDeleteResponse(
            nome=model.nome,
            message="Receita excluido com sucesso!"
        )

# -------------------------- EDIT -------------------------------------

@router.put("/{receita_id}", response_model=ReceitaEditResponse)
def edit_receita(receita_id: int, receita: ReceitaEdit, db: Session = Depends(get_db)):
        model = db.query(Receita).filter(Receita.id == receita_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Receita não encontrada.")

        for key, value in receita.model_dump(exclude_unset=True).items():
            setattr(model, key, value)

        db.commit()
        return TipoReceitaEditResponse(
            nome=model.nome,
            message="Receita atualizada com sucesso!"
        )

# -------------------------- LIST -------------------------------------

@router.get("/list/{receita_id}", response_model=List[ReceitaListResponse])
def list_receita(db: Session = Depends(get_db)):
    receitas = db.query(Receita).all()
    return receitas

# -------------------------- VIEW -------------------------------------

@router.get("/{receita_id}", response_model=ReceitaViewResponse)
def get_receita(receita_id: int, db: Session = Depends(get_db)):
        model = db.query(Receita).filter(Receita.id == receita_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Tipo de Gasto não encontrado.")

        return ReceitaViewResponse(
            id=model.id,
            nome=model.nome,
            valor=model.valor,
            data=model.data,
            descricao=model.descricao,
            eh_fixo=model.eh_fixo
        )
