import random

canais = ["Google","Meta","Tiktok","Youtube"]

ROAS_INICIAL = {
    "Google":   4.2,
    "Meta":     3.1,
    "Tiktok":   2.4,
    "Youtube":  2.9
}

SATURACAO = {
    "Google":   0.00020,
    "Meta":     0.00010,
    "Tiktok":   0.00008,
    "Youtube":  0.00012
}

ORCAMENTO = 10_000
TAMANHO_POPULACAO = 20
MAX_GERACOES = 100
TAXA_MUTACAO = 0.2

def criar_estrategia_aleatoria():
    pesos = [random.randint(1, 10) for _ in range(4)]
    total = sum(pesos)
    percentuais = [round(p / total * 100) for p in pesos]
    percentuais[0] += 100 - sum(percentuais)
    return percentuais

estrategia_teste = criar_estrategia_aleatoria()
print(f"Exemplo: {estrategia_teste}")
print(f"Soma dos percentuais: {sum(estrategia_teste)}%\n")

def calcular_retorno(estrategia):
    retorno_total = 0
    for i, canal in enumerate(canais):
        investimento = ORCAMENTO * estrategia[i] / 100
        roas_efetivo = ROAS_INICIAL[canal] - SATURACAO[canal] * investimento
        roas_efetivo = max(0.5, roas_efetivo)
        retorno_total += investimento * roas_efetivo
    return round(retorno_total, 2)

estrategia_tudo_google = [100, 0, 0, 0]
estrategia_equilibrada = [25, 25, 25, 25]

print(f"Tudo no google: R${calcular_retorno(estrategia_tudo_google):>8,.2f}")
print(f"Divisão Igual: R${calcular_retorno(estrategia_equilibrada):>8,.2f}")
print(f"Aleatório: R${calcular_retorno(estrategia_teste):>8,.2f}")

def cruzar(pai1, pai2):
    ponto = random.randint(1, 3)
    filho = pai1[:ponto] + pai2[ponto:]
    diferenca = 100 - sum(filho)
    filho[0] = diferenca
    return filho

pai1 = criar_estrategia_aleatoria()
pai2 = criar_estrategia_aleatoria()
filho = cruzar(pai1, pai2)

print(f"Pai 1: {pai1} - R${calcular_retorno(pai1):>8,.0f}")
print(f"Pai 2: {pai2} - R${calcular_retorno(pai2):>8,.0f}")
print(f"Filho: {pai2} - R${calcular_retorno(filho):>8,.0f}")

def mutar(estrategia):
    nova = list(estrategia)
    origem, destino = random.sample(range(4), 2)
    transferencia = random.randint(5, 20)

    if nova[origem] - transferencia >= 1:
        nova[origem] -= transferencia
        nova[destino] += transferencia
    return nova
print(f"Antes da mutação: {estrategia_teste}")
print(f"Depois da mutação: {mutar(estrategia_teste)}")

populacao = [criar_estrategia_aleatoria() for _ in range(TAMANHO_POPULACAO)]

print(f"="*40)
print(f"BUSCANDO A MELHOR DIVISÃO DE VERBA...")
print(f"="*40)

for geracao in range(MAX_GERACOES):
    populacao.sort(key=calcular_retorno, reverse=True)
    melhor = populacao[0]
    retorno_atual = calcular_retorno(melhor)

    print(f"Geração {geracao:>3} | Melhor retorno: {retorno_atual:>9,.2f} | Estratégia: {melhor}")

    proxima_geracao = populacao[:4]

    while len(proxima_geracao) < TAMANHO_POPULACAO:
        pai1, pai2 = random.sample(populacao[:10], 2)
        filho = cruzar(pai1, pai2)

        if random.random() < TAXA_MUTACAO:
            filho = mutar(filho)
            proxima_geracao.append(filho)

    populacao = proxima_geracao

melhor = populacao[0]

print(f"="*40)
print(f"ESTRATÉGIA VENCEDORA PELO ALGORITMO: ")
print(f"="*40)

for i, canal in enumerate(canais):
    investimento = ORCAMENTO * melhor[i] / 100
    roas_efetivo = max(0.5, ROAS_INICIAL[canal] - SATURACAO[canal] * investimento)
    retorno = investimento * roas_efetivo
    print(f"{canal:<10} {melhor[i]:>4}% - R${investimento:<6,.2f} investidos"
          f"(ROAS efetivo: {roas_efetivo:.2f}x) - R${retorno:<7,.0f}")
    print(f"="*40)
    print(f"('TOTAL':<10) {'100':<4}% - R${ORCAMENTO:<6,} investidos"
          f"                    - R4{calcular_retorno(melhor):7,.0f}")
    print(f"\nROAS médio final: {}")
    