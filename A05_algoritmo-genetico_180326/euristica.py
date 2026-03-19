import random
#  DEFINIÇÃO
# LISTAR 20 CARACTERISTICAS DE POSTS VIRAIS

NOMES_CARACTERISTICAS = [
    "QUALIDADE 4K",
    "VIDEO CURTO",
    "LEGENDA CURTA",
    "USO DE HASHTAG TREND",
    "AUDIO VIRAL",
    "CORES VIBRANTES",
    "PRESENÇA DE ROSTO HUMANO",
    "CTA (CALL TO ACTION)",
    "LEGENDA EMBUTIDA",
    "POSTADO EM HORÁRIO DE PICO",
    "COLLAB COM OUTRO PULICO",
    "RESPONDE AOS COMENTÁRIOS",
    "USO DE ENQUETE",
    "THUMB ATRAENTE",
    "TEMA QUE DESPERTA CURIOSIDADE",
    "TUTORIAL/EDUCATIVO",
    "CENÁRIO ESTÉTICO",
    "CORTE RÁPIDO EDIÇÃO",
    "TRILHA SONORA SINCRONIZADA"
    ]

# ALVO_VIRAL = [1] * len(NOMES_CARACTERISTICAS)
ALVO_VIRAL = [1] * 20
# print(ALVO_VIRAL)

TAMANHO_POPULACAO = 20
MAX_GERACOES = 100
TAXA_MUTACAO = 0.1

def criar_post_aleatorio():
    return [random.randint(0, 1) for _ in range(20)] 

post_teste = criar_post_aleatorio()
# print(f"Post teste: {post_teste}")

# FITNESS - QUÃO PARECIDO É COM O INDIVÍDUO IDEAL

def calcular_engajamento(post):
    return sum(1 for p, a in zip(post, ALVO_VIRAL) if p == a)

# print(f"Engajamento teste: {calcular_engajamento(post_teste)}")

# CROSSOVER

def fusao_de_post(pai1, pai2):
    ponto = random.randint(1, 10)
    return pai1[:ponto] + pai2[ponto:]

post_testeII = criar_post_aleatorio()
# print(f"Post teste II: {post_testeII}")
# print(f"Engajamento teste II: {calcular_engajamento(post_testeII)}")

# print(f"Fusao teste: {fusao_de_post(post_teste, post_testeII)}")


# MUTAÇÃO

def teste_de_novidade(post):
    novo_post = list(post)
    idx = random.randint(0, 19)
    novo_post[idx] = 1 - novo_post[idx]
    return novo_post

# print(teste_de_novidade(post_teste))

populacao = [criar_post_aleatorio() for _ in range(TAMANHO_POPULACAO)]

for geracao in range(MAX_GERACOES):
    populacao.sort(key=calcular_engajamento, reverse=True)
    melhor_post = populacao[0]
    nota_atual = calcular_engajamento(melhor_post)
    
    print(f"ciclo {geracao:02d} | Melhor post atual: {nota_atual}/20 ponntos")

    if nota_atual == 20:
        print(f"SUCESSO! A fórmula perfeita está no ciclo {geracao}")
        break

    proxima_geracao = populacao[:4]

    while len(proxima_geracao) < TAMANHO_POPULACAO:
        p1, p2 = random.sample(populacao[:10], 2)
        filho = fusao_de_post(p1, p2)

    if random.random() < TAXA_MUTACAO:
        filho = teste_de_novidade(filho)

    proxima_geracao.append(filho)

populacao = proxima_geracao

for i, status in enumerate(populacao[0]):
    legenda = "[ATIVADO]" if status == 1 else "[DESCARTADO]"
    print(f"{legenda:<15} | {NOMES_CARACTERISTICAS[i]}")

print("="*50)
print(f"Resultado: {calcular_engajamento(populacao[0])}/{len(NOMES_CARACTERISTICAS[0])}")