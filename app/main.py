import os
from fastapi import FastAPI
from app.routes.auth.router import router as auth_router
from app.routes.user.router import router as user_router
from app.database.database import Base, engine

app = FastAPI(
    title="PulseTrack API",
    description="API para gerenciamento de metas",
    version="1.0.0"
)

# Só cria as tabelas se não for ambiente de teste
if os.getenv("ENV") != "test":
    Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])


@app.get("/PulseTrack-API")
def root():
    return {"mensagem": "API PulseTrack está rodando!"}
