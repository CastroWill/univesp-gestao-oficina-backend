from fastapi import FastAPI

app = FastAPI(
    title="API Gestão Oficina",
    description="Sistema de agendamento para oficina mecânica",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "mensagem": "API da oficina funcionando!"
    }