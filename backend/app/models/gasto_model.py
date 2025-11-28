from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Gastos(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), min_length=3, max_length=255, nullable=False)
    valor = Column(DECIMAL, nullable=False)
    data = Column(Date, nullable=False)
    descricao = Column(String, min_length=3, max_length=255, nullable=True)
    eh_fixo = Column(Boolean, nullable=False)

    tipo_gasto_id = Column(Integer, ForeignKey("tipo_gasto.id"))
    tipo_gasto = relationship("TipoGasto")

