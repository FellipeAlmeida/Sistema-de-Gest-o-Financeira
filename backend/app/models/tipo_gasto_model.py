from database import Base
from sqlalchemy import Column, Integer, String

class TipoGasto(Base):
    __tablename__ = "tipo_gasto"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)



