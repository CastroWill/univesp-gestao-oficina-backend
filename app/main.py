from fastapi import FastAPI

from app.database.connection import engine
from app.models.agendamento import Agendamento


Agendamento.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Gestão Oficina",
    description="Sistema de gerenciamento de oficina",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "mensagem": "API funcionando!"
    }