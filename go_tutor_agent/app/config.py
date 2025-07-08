import os
from dotenv import load_dotenv

load_dotenv()

ACTIVE_MODEL_FAMILY = "gemini"


MODEL_FAMILY_CONFIGS = {
    "mistral": {

        "provider": "openai",
        "model_id": os.getenv("MISTRAL_MODEL_ID", "openrouter/mistralai/mistral-7b-instruct:free"),
        "api_key": os.getenv("OPENROUTER_API_KEY"),
        "api_base": "https://openrouter.ai/api/v1",
        "prompt_dir": "mistral_family",  
    },
    "gemini": {
        "provider": "google",
        "model_id": os.getenv("GEMINI_MODEL_ID", "gemini/gemini-1.5-flash-latest"),
        "api_key": os.getenv("GEMINI_API_KEY"),
        "api_base": None,
        "prompt_dir": "gemini_family", 
    },
    "openai": {
        "provider": "openai",
        "model_id": os.getenv("OPENAI_MODEL_ID", "gpt-3.5-turbo"),
        "api_key": os.getenv("OPENAI_API_KEY"),
        "api_base": None,
        "prompt_dir": "openai_family",
    }
}

active_config = MODEL_FAMILY_CONFIGS.get(ACTIVE_MODEL_FAMILY)

if not active_config:
    raise ValueError(f"Familia de modelo '{ACTIVE_MODEL_FAMILY}' no es válida. Opciones: {list(MODEL_FAMILY_CONFIGS.keys())}")

MODEL_ID = active_config.get("model_id")
MODEL_API_KEY = active_config.get("api_key")
MODEL_API_BASE = active_config.get("api_base")
ACTIVE_PROMPT_DIR_NAME = active_config.get("prompt_dir")

# Verificación de seguridad
if not all([MODEL_ID, MODEL_API_KEY, ACTIVE_PROMPT_DIR_NAME]):
    raise ValueError(f"Configuración incompleta para la familia '{ACTIVE_MODEL_FAMILY}'. Revisa tu .env y config.py")

print(f"✔️ [Config] Familia de Modelos Activa: {ACTIVE_MODEL_FAMILY}")
print(f"✔️ [Config] Modelo a usar: {MODEL_ID}")
print(f"✔️ [Config] Cargando prompts desde: app/agent/prompts/{ACTIVE_PROMPT_DIR_NAME}")