def analisar_energia(geracao, consumo):

    if consumo > geracao:
        return "ALERTA: consumo maior que geração"

    elif geracao > consumo:
        return "SUGESTÃO: armazenar energia excedente"

    else:
        return "Sistema equilibrado"


def modo_economia(energia, consumo):

    if energia < 50 and consumo > 60:
        return "MODO ECONOMIA ATIVADO"

    return "Consumo normal"