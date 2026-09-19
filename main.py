def validar_texto_obligatorio(texto: str, longitud_minima: int = 1) -> bool:
    """Valida que un texto no esté vacío y cumpla con la longitud mínima."""
    texto_limpio = texto.strip()
    return len(texto_limpio) >= longitud_minima