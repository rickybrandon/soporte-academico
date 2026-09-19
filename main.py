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
def registrar_solicitudes_lote(lista_solicitudes: list, nuevas_solicitudes: list) -> list:
    """Recibe una lista existente y agrega múltiples nuevas solicitudes."""
    lista_solicitudes.extend(nuevas_solicitudes)
    return lista_solicitudes
def buscar_solicitudes(lista_solicitudes: list, criterio: str) -> list:
    """Busca solicitudes por código de estudiante o por tipo de consulta."""
    criterio_limpio = criterio.strip().lower()
    resultados = []
    for sol in lista_solicitudes:
        if (sol.get("codigo") == criterio_limpio or 
            sol.get("tipo", "").lower() == criterio_limpio):
            resultados.append(sol)
    return resultados
def calcular_estadisticas(lista_solicitudes: list) -> dict:
    """Calcula el total de solicitudes y la distribución por prioridad."""
    total = len(lista_solicitudes)
    conteo_prioridad = {"Alta": 0, "Media": 0, "Baja": 0}
    
    for sol in lista_solicitudes:
        prioridad = sol.get("prioridad", "Baja")
        if prioridad in conteo_prioridad:
            conteo_prioridad[prioridad] += 1
            
    return {
        "total": total,
        "por_prioridad": conteo_prioridad
    }