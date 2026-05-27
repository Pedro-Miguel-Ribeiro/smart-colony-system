from dados import sistema_colonia
from decisoes import analisar_energia, modo_economia
from previsao import prever_energia


geracao = (
    sistema_colonia["energia"]["solar"] +
    sistema_colonia["energia"]["eolica"]
)

consumo = (
    sistema_colonia["consumo"]["suporte_vida"] +
    sistema_colonia["consumo"]["iluminacao"] +
    sistema_colonia["consumo"]["laboratorio"]
)

print("=== SISTEMA DA COLÔNIA ===")

print(analisar_energia(geracao, consumo))

print(
    modo_economia(
        sistema_colonia["energia"]["bateria"],
        consumo
    )
)

vento = sistema_colonia["clima"]["vento"]

previsao = prever_energia(vento)

print(f"Previsão de energia eólica: {previsao}")