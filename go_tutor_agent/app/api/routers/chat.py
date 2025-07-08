from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel
from app.services.agent_services import process_user_message
from smolagents import CodeAgent 
router = APIRouter(prefix="/api/v1", tags=["Chat"])

class ChatRequest(BaseModel):
    message: str
    user_id: str = "default user"

class ChatResponse(BaseModel):
    reply: str


def get_agent(request: Request) -> CodeAgent:
    """
    Esta es una dependencia de FastAPI.
    Obtiene la instancia del agente en app.state.
    """
    return request.app.state.agent


@router.post("/chat", response_model=ChatResponse)
async def handle_chat(
    request: ChatRequest, 
    agent_instance: CodeAgent = Depends(get_agent)
):
    if not request.message:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")

    print(f"Mensaje recibido '{request.user_id}: {request.message}'")

    
    agent_reply = process_user_message(
        user_message=request.message, 
        agent_instance=agent_instance
    )

    return ChatResponse(reply=agent_reply)