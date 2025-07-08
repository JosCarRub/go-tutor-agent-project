import litellm
from smolagents import tool
from app.config import MODEL_ID, MODEL_API_KEY, MODEL_API_BASE

@tool
def translate_text(text_to_translate: str) -> str:
    """
    Translates a given text into Spanish. Use this tool when you have a final
    answer in English and need to present it to the user in Spanish.

    Args:
        text_to_translate (str): The English text to be translated.
    """
    if not text_to_translate or not isinstance(text_to_translate, str):
        return "Error: No valid text provided for translation."

    print(f"🔄 [Tool:Translator] Traduciendo texto...")

    try:
        messages = [
            {
                "role": "system",
                "content": "You are an expert English to Spanish translator. Translate the user's text accurately and naturally. Do not add any extra comments, introductions, or formatting. Only provide the translated text."
            },
            {
                "role": "user",
                "content": text_to_translate
            }
        ]
        
        model_params = {
            "model": MODEL_ID,
            "messages": messages,
            "api_key": MODEL_API_KEY,
            "temperature": 0.1, 
        }
        if MODEL_API_BASE:
            model_params["api_base"] = MODEL_API_BASE

        response = litellm.completion(**model_params)
        
        translated_text = response.choices[0].message.content.strip()
        print("✅ [Tool:Translator] Traducción completada.")
        return translated_text

    except Exception as e:
        print(f"❌ [Tool:Translator] Error durante la traducción: {e}")
        return text_to_translate