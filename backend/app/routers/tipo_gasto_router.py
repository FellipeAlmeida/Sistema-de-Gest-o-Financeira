from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.tipo_gasto_model import TipoGasto
from app.schemas.tipo_gasto_schema import TipoGastoCreate, TipoGastoCreateResponse
from app.database import get_db

router = APIRouter(
    prefix="/tipo_gasto",
    tags=["01. tipo_gasto"]
)

@router.post("", response_model=TipoGastoCreateResponse)
def criar_tipo_gasto(payload: TipoGastoCreate, db: Session = Depends(get_db)):
    try:
        model = TipoGasto(**payload.model_dump())
        db.add(model)
        db.commit()
        db.refresh(model)
        return TipoGastoCreateResponse(id=model.id, message="Tipo de Gasto criado com sucesso!")
    except Exception as e:
        print(e)
