from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routers import chat
from app.agent.agent import get_agent_instance
from prometheus_fastapi_instrumentator import Instrumentator

# @asynccontextmanager permite ejecutar código durante el arranque y apagado 
@asynccontextmanager
async def lifespan(app: FastAPI):

    print("🚀 [Main] Iniciando aplicación...")

    agent_singleton = get_agent_instance()
    
    app.state.agent = agent_singleton
    print("✔️ [Main] Agente singleton creado y almacenado en el estado de la aplicación.")
    
    yield # La aplicación se ejecuta aquí
    
    
    print("🛑 [Main] Apagando aplicación...")

app = FastAPI(
    title="GoAgentTutor API",
    description="Servicio backend para agente de IA GoAgentTutor",
    version="0.2.0",
    lifespan=lifespan
)

Instrumentator().instrument(app).expose(app)

app.include_router(chat.router)

@app.get("/")
async def root(): 
    return {"message": "Hola desde GoAgentTutor"}

@app.get("/health")
async def health_check():   
    return {"status": "ok"}