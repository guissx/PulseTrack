from fastapi import FastAPI

app = FastAPI(
    title="PulseTrack API",
    description="API para gerenciamento de metas ",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"mensagem": "API PulseTrack está rodando!"}
