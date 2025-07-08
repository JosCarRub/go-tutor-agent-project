# go_tutor_agent/app/tools/code_executor.py
import os
import requests
from smolagents import tool

GO_EXECUTOR_URL = os.getenv("GO_EXECUTOR_URL")

@tool
def execute_go_code(code: str) -> str:
    """
    Envía un bloque de código Go a un microservicio de ejecución seguro y devuelve la salida.

    Args:
        code (str): El código Go completo a ejecutar.
    """
    
    if not GO_EXECUTOR_URL:
        return "Error de configuración: La variable de entorno GO_EXECUTOR_URL no está definida."

    print(f"🚀 [Tool:Executor] Enviando código al servicio remoto en {GO_EXECUTOR_URL}...")
    try:
        response = requests.post(
            f"{GO_EXECUTOR_URL}/execute",
            json={"code": code},
            timeout=20  
        )
        
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("error"):
            error_output = data["error"]
            print(f"❌ [Tool:Executor] El servicio remoto devolvió un error:\n{error_output}")
            return f"El código falló al ejecutarse. Error:\n---\n{error_output}"
        else:
            output = data.get("output", "")
            print(f"✅ [Tool:Executor] Ejecución remota exitosa. Salida:\n{output}")
            return f"Ejecución completada con éxito. Salida:\n---\n{output}"

    except requests.exceptions.Timeout:
        return "Error: La petición al servicio de ejecución de código ha expirado (timeout)."
    except requests.exceptions.RequestException as e:
        return f"Error de red al comunicarse con el servicio de ejecución: {e}"
    except Exception as e:
        return f"Error inesperado al procesar la ejecución del código: {e}"