from app.agent.prompt_builder import SYSTEM_PROMPT
from smolagents import CodeAgent
import litellm

def process_user_message(user_message: str, agent_instance: CodeAgent) -> str:
    """
    Esta es la función principal del servicio.
    Orquesta la interacción con el agente que recibe como parámetro.
    """
    
    task = f"{SYSTEM_PROMPT}\n\nPregunta del usuario: {user_message}"
    
    print("🚀 [Service] Ejecutando agente con la siguiente tarea...")
    
    try:
        final_plan_or_result = agent_instance.run(task=task)
        
        if hasattr(final_plan_or_result, 'actions') and final_plan_or_result.actions:
            print("ℹ️ [Service] Se encontró un plan con acciones.")
            for action in final_plan_or_result.actions:
                if action.tool_name == "final_answer":
                    return str(action.tool_output)
        elif final_plan_or_result:
            print("ℹ️ [Service] Se encontró una respuesta directa.")
            return str(final_plan_or_result)
        return "El agente procesó la solicitud, pero no generó una respuesta final."

    except Exception as e:

        if isinstance(e, litellm.RateLimitError) or (hasattr(e, '__cause__') and isinstance(e.__cause__, litellm.RateLimitError)):
            print("🟡 [Service] Límite de peticiones alcanzado (detectado en la capa de servicio). Generando mensaje personalizado.")
            user_friendly_message = (
                "¡Vaya! Parece que hoy has hecho muchas preguntas y hemos alcanzado "
                "nuestro límite de consultas diarias debido a la alta demanda. "
                "Por favor, vuelve a intentarlo mañana. ¡Gracias por tu comprensión!"
            )
            return user_friendly_message
        else:

            print(f"💥 [Service] Error CRÍTICO durante la ejecución del agente: {e}")
            return "Ha ocurrido un error inesperado al procesar tu solicitud. Por favor, inténtalo de nuevo más tarde."