import chromadb
from chromadb.utils import embedding_functions

print("ℹ️ [Memory] Inicializando el cliente de la base de datos vectorial...")

# 1. Creamos un cliente de ChromaDB.
#    `PersistentClient` significa que guardará los datos en el disco,
#    en una carpeta llamada 'chroma_db' que se creará en la raíz del proyecto.
#    de este modo, la memoria sobrevive entre reinicios de la aplicación.
client = chromadb.PersistentClient(path="./chroma_db")

# 2. Definimos la función de embedding.
#    Le decimos a ChromaDB que use un modelo de SentenceTransformer.
#    La primera vez que se ejecute, descargará el modelo 'all-MiniLM-L6-v2'.
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# 3. Obtenemos o creamos una "colección".
#    colección = tabla en una base de datos SQL.
#    `embedding_function` para que sepa cómo
#    convertir el texto que le demos en vectores.
collection = client.get_or_create_collection(
    name="go_docs_collection",
    embedding_function=embedding_function
)

print("✔️ [Memory] Cliente de ChromaDB y colección 'go_docs_collection' listos.")