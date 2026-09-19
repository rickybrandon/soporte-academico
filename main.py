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
def cambiar_estado_solicitud(lista_solicitudes: list, codigo_ticket: str, nuevo_estado: str) -> bool:
    """Busca una solicitud por su código de ticket y actualiza su estado."""
    for sol in lista_solicitudes:
        if sol.get("ticket") == codigo_ticket:
            sol["estado"] = nuevo_estado
            return True
    return False
def main():
    """Función principal del sistema."""
    solicitudes = []
    correlativo = 1
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            codigo = input("Código de estudiante: ").strip()
            if not validar_texto_obligatorio(codigo):
                print("Error: El código no es válido.")
                continue
                
            tipo = input("Tipo de consulta (matricula/pagos/constancia/plataforma/otro): ").strip()
            if not validar_tipo_consulta(tipo):
                print("Error: Tipo de consulta no permitido.")
                continue
                
            desc = input("Descripción de la solicitud: ").strip()
            urgencia_str = input("Nivel de urgencia (1-5): ").strip()
            urgencia = int(urgencia_str) if urgencia_str.isdigit() else 1
            
            ticket = generar_codigo_ticket(correlativo)
            prioridad = determinar_prioridad(urgencia)
            
            nueva_sol = {
                "ticket": ticket,
                "codigo": codigo,
                "tipo": tipo,
                "descripcion": desc,
                "urgencia": urgencia,
                "prioridad": prioridad,
                "estado": "Pendiente"
            }
            
            solicitudes.append(nueva_sol)
            correlativo += 1
            print(f"✅ Solicitud registrada con éxito. Ticket: {ticket} | Prioridad: {prioridad}")
            
        elif opcion == "2":
            if not solicitudes:
                print("No hay solicitudes registradas.")
            else:
                print("\n--- LISTA DE SOLICITUDES ---")
                for s in solicitudes:
                    print(f"[{s['ticket']}] Estudiante: {s['codigo']} | Tipo: {s['tipo']} | Prioridad: {s['prioridad']} | Estado: {s['estado']}")
                    
        elif opcion == "3":
            print("¡Gracias por utilizar el Módulo de Atención!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
