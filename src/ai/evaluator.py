import re

def evaluar_regex(regex, positivos, negativos):
    def coincide(cadena):
        return re.fullmatch(regex, cadena) is not None

    positivos_bien = all(coincide(ej) for ej in positivos)
    negativos_bien = all(not coincide(ej) for ej in negativos)

    return {
        "regex": regex,
        "positivos_ok": positivos_bien,
        "negativos_ok": negativos_bien,
        "validez": positivos_bien and negativos_bien
    }
