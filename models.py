from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)

class CodigoAluno(Base):
    __tablename__ = "codigos"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String)