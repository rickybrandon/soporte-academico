def validar_texto_obligatorio(texto: str, longitud_minima: int = 1) -> bool:
    """Valida que un texto no esté vacío y cumpla con la longitud mínima."""
    texto_limpio = texto.strip()
    return len(texto_limpio) >= longitud_minima
TIPOS_PERMITIDOS = ["matricula", "pagos", "constancia", "plataforma", "otro"]

def validar_tipo_consulta(tipo: str) -> bool:
    """Valida si el tipo de consulta pertenece a la lista permitida."""
    return tipo.strip().lower() in TIPOS_PERMITIDOS
def mostrar_menu():
    """Muestra el menú principal en consola."""
    print("\n============================================")
    print("   SOPORTE ACADÉMICO - MÓDULO DE ATENCIÓN   ")
    print("============================================")
    print("1. Registrar nueva solicitud")
    print("2. Ver solicitudes registradas")
    print("3. Salir")
    print("============================================")
    def determinar_prioridad(urgencia: int) -> str:
    """Determina la prioridad de la solicitud según el nivel de urgencia (1 a 5)."""
    if urgencia >= 4:
        return "Alta"
    elif urgencia >= 2:
        return "Media"
    else:
        return "Baja"
    def generar_codigo_ticket(correlativo: int, prefijo: str = "SA") -> str:
    """Genera un código único de ticket formateado como PREFIJO-000X."""
    return f"{prefijo}-{correlativo:04d}"