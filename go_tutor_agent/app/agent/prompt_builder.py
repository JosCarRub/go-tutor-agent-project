import os
from app.config import ACTIVE_PROMPT_DIR_NAME
from app.tools.registry import ALL_TOOLS

def load_prompt_from_file(file_path: str) -> str:
    """Carga el contenido de un archivo de prompt de forma segura."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"🚨 ADVERTENCIA: No se encontró el archivo de prompt en {file_path}")
        return "" 


PROMPTS_BASE_DIR = os.path.join(os.path.dirname(__file__), 'prompts')
PROMPT_COMMON_DIR = os.path.join(PROMPTS_BASE_DIR, 'common')
PROMPT_PROVIDER_DIR = os.path.join(PROMPTS_BASE_DIR, ACTIVE_PROMPT_DIR_NAME)


main_prompt = load_prompt_from_file(os.path.join(PROMPT_PROVIDER_DIR, 'main_system.txt'))

tools_header = load_prompt_from_file(os.path.join(PROMPT_COMMON_DIR, 'tools_header.txt'))

final_reminder = load_prompt_from_file(os.path.join(PROMPT_COMMON_DIR, 'final_reminder.txt'))

tool_descriptions = []
for tool in ALL_TOOLS:
    tool_name = tool.name 
    prompt_file_name = f"tool_{tool_name}.txt"
    

    tool_prompt_path = os.path.join(PROMPT_PROVIDER_DIR, prompt_file_name)
    if not os.path.exists(tool_prompt_path):
        tool_prompt_path = os.path.join(PROMPT_COMMON_DIR, prompt_file_name)
        
    description = load_prompt_from_file(tool_prompt_path)
    if description:
        tool_descriptions.append(description)

print(f"ℹ️ [Prompt Builder] Cargadas {len(tool_descriptions)} descripciones de herramientas.")

SYSTEM_PROMPT = "\n".join([
    main_prompt,
    tools_header,
    *tool_descriptions,
    final_reminder, 
]).strip()