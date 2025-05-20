from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, Base
import models, schemas

app = FastAPI()

# CORS liberado para qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria as tabelas
Base.metadata.create_all(bind=engine)

# Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="E-mail já registrado")
    novo_usuario = models.User(**user.dict())
    db.add(novo_usuario)
    db.commit()
    return {"mensagem": "Usuário cadastrado com sucesso"}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(
        models.User.email == user.email,
        models.User.senha == user.senha
    ).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"mensagem": "Login bem-sucedido"}

@app.post("/enviar_codigo")
def enviar_codigo(dados: schemas.Codigo, db: Session = Depends(get_db)):
    novo_codigo = models.CodigoAluno(codigo=dados.codigo)
    db.add(novo_codigo)
    db.commit()
    return {"resultado": "Código recebido e salvo!"}