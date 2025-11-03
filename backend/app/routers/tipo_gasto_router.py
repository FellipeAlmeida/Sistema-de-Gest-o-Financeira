from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.tipo_gasto_model import TipoGasto
from app.schemas.tipo_gasto_schema import TipoGastoCreate, TipoGastoCreateResponse
from app.database import get_db
from app.schemas.tipo_gasto_schema import TipoGastoDelete, TipoGastoDeleteResponse

router = APIRouter(
    prefix="/tipo_gasto",
    tags=["01. tipo_gasto"]
)

# -------------------------- CREATE -------------------------------------

@router.post("", response_model=TipoGastoCreateResponse)
def criar_tipo_gasto(payload: TipoGastoCreate, db: Session = Depends(get_db)):
    try:
        model = TipoGasto(**payload.model_dump()) # model_dump transforma os dados em dicionário python para o sqlalchemy
        db.add(model)
        db.commit()
        db.refresh(model)
        return TipoGastoCreateResponse(id=model.id, message="Tipo de Gasto criado com sucesso!")
    except Exception as e:
        print(e)

# -------------------------- DELETE -------------------------------------

@router.delete("/{tipo_gasto_id}", response_model=TipoGastoDeleteResponse)
def delete_tipo_gasto(tipo_gasto_id: int, db: Session = Depends(get_db)):
        model = db.query(TipoGasto).filter(TipoGasto.id == tipo_gasto_id).first()

        if not model:
            raise HTTPException(status_code=404, detail="Tipo de Gasto não encontrado.")

        db.delete(model)
        db.commit()
        return TipoGastoDeleteResponse(
            id=model.id,
            message="Tipo de Gasto excluido com sucesso!"
        )



