from app.agent.memory import collection
import argparse

def clear_all_data():
    print("ADVERTENCIA: Estás a punto de eliminar TODOS los datos de la colección.")
    confirm = input("Escribe 'y' para continuar: ")
    if confirm == "y":
        ids = collection.get()["ids"]
        if ids:
            collection.delete(ids=ids)
            print(f"✅ {len(ids)} documentos eliminados.")
        else:
            print("ℹ️ La colección ya está vacía.")
    else:
        print("Operación cancelada.")

def delete_by_source(source_url: str):
    print(f"Intentando eliminar todos los documentos de la fuente: {source_url}")
    collection.delete(where={"source": source_url})
    print(f"✅ Documentos de '{source_url}' eliminados.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Herramienta de gestión para ChromaDB.")
    parser.add_argument("--clear-all", action="store_true", help="Elimina todos los datos de la colección.")
    parser.add_argument("--delete-source", type=str, help="Elimina todos los documentos de una URL específica.")
    
    args = parser.parse_args()

    if args.clear_all:
        clear_all_data()
    elif args.delete_source:
        delete_by_source(args.delete_source)
    else:
        print("Por favor, especifica una acción. Usa --help para ver las opciones.")