from fastapi import FastAPI
from app.routes import triagem

app = FastAPI(
    title="API de Triagem Psicossocial Gestacional",
    description="API para apoio à triagem de risco psicossocial em gestantes. Não substitui avaliação profissional.",
    version="1.0.0"
)

app.include_router(triagem.router, prefix="/v1/triagem", tags=["Triagem"])


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API funcionando"
    }