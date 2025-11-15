from app.database import Base
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

class Receita(Base):
    __tablename__ = "receita"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    valor = Column(DECIMAL, nullable=False)
    data = Column(Date)
    descricao = Column(Text)
    eh_fixo = Column(Boolean, nullable=False)

    tipo_receita_id = Column(Integer, ForeignKey("tipo_receita.id"))
    tipo_receita = relationship("TipoReceita")

