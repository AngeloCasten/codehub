from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str

class UserLogin(BaseModel):
    email: str
    senha: str

class Codigo(BaseModel):
    codigo: str