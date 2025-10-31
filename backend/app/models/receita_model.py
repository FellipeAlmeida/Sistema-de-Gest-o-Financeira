from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

class Gastos(BaseModel):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    valor = Column(DECIMAL, nullable=False)
    data = Column(Date)
    descricao = Column()
    eh_fixo = Column(Boolean, nullable=False)

    tipo_receita_id = Column(Integer, ForeignKey("tipo_receita.id"))
    tipo_receita = relationship("TipoReceita")

