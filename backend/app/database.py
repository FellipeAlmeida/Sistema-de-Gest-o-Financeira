from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

# cria conexão com o banco
engine = create_engine(DATABASE_URL)

# sessão pra lidar com atualizações
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# abre, "entrega" para a rota e fecha o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()