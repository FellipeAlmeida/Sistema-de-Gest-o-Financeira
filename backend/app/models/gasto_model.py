from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.database import Base


class Gastos(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    valor = Column(DECIMAL, nullable=False)
    data = Column(Date)
    descricao = Column()
    eh_fixo = Column(Boolean, nullable=False)

    tipo_gasto_id = Column(Integer, ForeignKey("tipo_gasto.id"))
    tipo_gasto = relationship("TipoGasto")

