from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.receita_model import Receita
from schemas.receita_schema import ReceitaCreateResponse, ReceitaCreate

from schemas.receita_schema import ReceitaDeleteResponse, ReceitaEditResponse, ReceitaEdit, \
    ReceitaListResponse, ReceitaViewResponse

from models.receita_model import Receita
from schemas.receita_schema import ReceitaCreateResponse, ReceitaDeleteResponse, ReceitaEditResponse, \
    ReceitaViewResponse, ReceitaListResponse

from schemas.receita_schema import ReceitaCreate, ReceitaEdit

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

        return ReceitaCreateResponse(
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
            id=model.id,
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
        return ReceitaEditResponse(
            nome=model.nome,
            tipo_receita_id=model.tipo_receita_id,
            valor=model.valor,
            data=model.data,
            descricao=model.descricao,
            eh_fixo=model.eh_fixo,
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
            raise HTTPException(status_code=404, detail="Receita de Gasto não encontrado.")

        return ReceitaViewResponse(
            id=model.id,
            nome=model.nome,
            valor=model.valor,
            data=model.data,
            descricao=model.descricao,
            eh_fixo=model.eh_fixo
        )
