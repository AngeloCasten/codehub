from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://bd_codigos_alunos_user:OOVhRqH8vZFM5rl3QAyiAyLI7nqnSKWl@dpg-d0m9iv0gjchc739mea2g-a/bd_codigos_alunos"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()