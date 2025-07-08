from smolagents import tool

@tool
def get_creator_information() -> str:
    """
    Devuelve información sobre el creador de este sistema de IA.
    Usa esta herramienta SOLAMENTE si el usuario pregunta explícitamente
    quién me creó, quién es el desarrollador, o cómo contactar al autor.
    """
    info = """
    Este sistema de agentes fue diseñado y desarrollado por José Carlos Rubio.
    - GitHub: https://github.com/JosCarRub
    - Portfolio: josecarlosdev.com (En construcción!)
    - Contacto para proyectos de IA y sistemas de agentes: contacto@josecarlosdev.com
    """
    return info.strip()