def generar_regex_heuristica(ejemplos_positivos):
    if not ejemplos_positivos:
        return ""

    # Prefijo común
    prefijo = ejemplos_positivos[0]
    for ejemplo in ejemplos_positivos[1:]:
        while not ejemplo.startswith(prefijo) and prefijo:
            prefijo = prefijo[:-1]

    # Sufijo común
    sufijo = ejemplos_positivos[0]
    for ejemplo in ejemplos_positivos[1:]:
        while not ejemplo.endswith(sufijo) and sufijo:
            sufijo = sufijo[1:]

    # Resultado tentativo
    if prefijo and sufijo:
        return f"^{prefijo}.*{sufijo}$"
    elif prefijo:
        return f"^{prefijo}.*"
    elif sufijo:
        return f".*{sufijo}$"
    else:
        return ".*"
