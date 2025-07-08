import litellm
import requests
from bs4 import BeautifulSoup
from smolagents import tool
from app.config import MODEL_ID, MODEL_API_KEY, MODEL_API_BASE 
from app.agent.memory import collection

def _scrape_and_chunk_text(url: str, chunk_size: int = 1500, chunk_overlap: int = 200) -> list[str]:
    """Función auxiliar privada para scrapear y trocear texto."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
        element.decompose()
    text = soup.get_text(separator='\n', strip=True)
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size - chunk_overlap)]

@tool
def index_url(url: str) -> str:
    """
    Descarga, procesa y añade el contenido de una URL a la base de conocimiento para futuras búsquedas.
    Úsala para 'aprender' o 'estudiar' un documento antes de hacer preguntas sobre él.

    Args:
        url (str): La URL que se debe procesar e indexar.
    """
    try:
        existing_docs = collection.get(where={"source": url}, limit=1)
        if existing_docs['ids']:
            return f"Información: La URL '{url}' ya ha sido indexada previamente."

        print(f"ℹ️ [Tool:Indexer] Indexando nueva URL: {url}")
        chunks = _scrape_and_chunk_text(url)
        if not chunks:
            return f"Error: No se pudo extraer contenido de la URL: {url}"
        
        ids = [f"{url}#{i}" for i in range(len(chunks))]
        metadatas = [{"source": url} for _ in range(len(chunks))]
        
        collection.add(documents=chunks, metadatas=metadatas, ids=ids)
        success_message = f"Éxito: La URL '{url}' ha sido procesada y añadida a la base de conocimiento con {len(chunks)} trozos."
        print(f"✅ {success_message}")
        return success_message
    except Exception as e:
        error_message = f"Error al indexar la URL '{url}': {e}"
        print(f"❌ [Tool:Indexer] {error_message}")
        return error_message

@tool
def search_knowledge_base(query: str) -> str:
    """
    Busca en la base de conocimiento y utiliza un LLM para sintetizar
    una respuesta coherente a partir de los resultados encontrados.

    Args:
        query (str): La pregunta específica o el tema a buscar.
    """
    try:
        print(f"🔍 [Tool:Searcher] Buscando en la base de conocimiento: '{query}'...")
        results = collection.query(
            query_texts=[query],
            n_results=5, 
        )
        
        if not results or not results['documents'][0]:
            return f"No se encontró información relevante para '{query}' en la base de conocimiento."

        context = "\n---\n".join(results['documents'][0])

        synthesis_prompt = f"""
        Based on the following context, please provide a concise and interesting answer to the user's query.
        The answer should be a direct response, not a summary of the context.

        CONTEXT:
        ---
        {context}
        ---
        USER'S QUERY: {query}

        CONCISE ANSWER:
        """
        
        print("🧠 [Tool:Searcher] Sintetizando respuesta a partir del contexto...")
        
        model_params = {
            "model": MODEL_ID,
            "messages": [{"role": "user", "content": synthesis_prompt}],
            "api_key": MODEL_API_KEY,
        }
        if MODEL_API_BASE:
            model_params["api_base"] = MODEL_API_BASE

        response = litellm.completion(**model_params)
        synthesized_answer = response.choices[0].message.content.strip()

        return synthesized_answer

    except Exception as e:
        error_message = f"Error durante la búsqueda o síntesis en la base de conocimiento: {e}"
        print(f"❌ [Tool:Searcher] {error_message}")
        return error_message