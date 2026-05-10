from fastapi import FastAPI

from app.database.connection import engine
from app.models.agendamento import Agendamento
from app.routes.agendamento import router as agendamento_router


Agendamento.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Gestão Oficina",
    description="Sistema de gerenciamento de oficina",
    version="1.0.0"
)

app.include_router(agendamento_router)


@app.get("/")
def home():
    return {
        "mensagem": "API funcionando!"
    }