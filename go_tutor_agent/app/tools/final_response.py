from smolagents import tool


@tool
def final_answer(answer: str) -> str:
    """
    Usa esta herramienta para dar tu respuesta final y directa al usuario.
    Esta es la última acción que realizarás en tu plan.

    Args:
        answer (str): El texto completo de la respuesta que se le debe dar al usuario.
    """
    return answer