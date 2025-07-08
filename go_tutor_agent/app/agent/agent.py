from smolagents import CodeAgent, LiteLLMModel
from .prompt_builder import SYSTEM_PROMPT
from app.tools.registry import ALL_TOOLS 
from app.config import MODEL_ID, MODEL_API_KEY, MODEL_API_BASE

def get_agent_instance() -> CodeAgent:
    """
    Fábrica que construye y devuelve una instancia del agente bajo demanda.
    Esta es la única función que el resto de la aplicación usará.
    """
    print("ℹ️ [Agent Factory] Solicitada nueva instancia de agente...")
    model_params = {
        "model_id": MODEL_ID,
        "api_key": MODEL_API_KEY,
        "temperature": 0.3,
    }
    if MODEL_API_BASE:
        model_params["api_base"] = MODEL_API_BASE

    llm_model = LiteLLMModel(**model_params)
    
    agent = CodeAgent(
        model=llm_model,
        tools=ALL_TOOLS,
        verbosity_level=2,
    )
    print("✔️ [Agent Factory] Instancia de GoAgentTutor creada y lista.")
    return agent