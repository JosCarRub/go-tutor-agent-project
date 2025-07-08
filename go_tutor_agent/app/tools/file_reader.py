# app/tools/file_reader.py

import os
from smolagents import tool

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAFE_DATA_DIRECTORY = os.path.normpath(os.path.join(BASE_DIR, '..', '..', 'data'))

@tool
def read_file_content(file_path: str) -> str:
    """
    Lee el contenido de un archivo de lección de Go.
    Puedes pasar el nombre exacto del archivo o un tema clave (ej: 'variables', 'concurrencia', 'interfaces') y buscaré el archivo más relevante.

    Args:
        file_path (str): Tema a buscar.
    """
    try:

        full_path_exact = os.path.normpath(os.path.join(SAFE_DATA_DIRECTORY, file_path))
        if os.path.exists(full_path_exact) and os.path.isfile(full_path_exact):
            if not full_path_exact.startswith(SAFE_DATA_DIRECTORY):
                return f"Error de seguridad: Acceso denegado a '{file_path}'."
            with open(full_path_exact, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"✅ [Tool:read_file_content] Leído por coincidencia exacta: {full_path_exact}")
            return content


        print(f"ℹ️ [Tool:read_file_content] No se encontró coincidencia exacta. Buscando por palabra clave: '{file_path}'")
        query_keyword = file_path.split('_')[0].lower() 
        
        for filename in os.listdir(SAFE_DATA_DIRECTORY):
            if filename.endswith(".md") and query_keyword in filename.lower():
                full_path_relevant = os.path.normpath(os.path.join(SAFE_DATA_DIRECTORY, filename))
                if not full_path_relevant.startswith(SAFE_DATA_DIRECTORY):
                    continue 
                
                with open(full_path_relevant, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                print(f"✅ [Tool:read_file_content] Leído por coincidencia de palabra clave: {full_path_relevant}")
                return f"Nota del Lector de Archivos: Devolviendo contenido del archivo más relevante encontrado: '{filename}'\n\n---\n\n{content}"

        return f"Error: No se encontró ningún archivo de lección relevante para la consulta '{file_path}'."

    except Exception as e:
        return f"Error inesperado al leer el archivo para la consulta '{file_path}': {e}"