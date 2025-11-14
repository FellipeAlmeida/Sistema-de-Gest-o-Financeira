from app.database import Base
from sqlalchemy import Column, Integer, String

class TipoReceita(Base):
    __tablename__ = "tipo_receita"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)



