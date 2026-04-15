
# ==================================| AUTORES |================================
# =============================| Tema: Seleção de Equipes
# =============================| by Thiago & Bryan.
# =============================================================================
# 
# =============================================================================
# MONTAGEM DE TIME DE PROJETO
# =============================================================================
# Problema: Selecionar um subconjunto de N pessoas disponíveis, cada uma com
# habilidades e custos distintos, de forma a cobrir as habilidades necessárias
# para o projeto dentro de um orçamento limite — maximizando a "performance"
# do time.
# 
# Técnicas utilizadas:
#   1. Modelagem como Espaço de Estados
#   2. Busca em Largura (BFS)
#   3. Heurística de cobertura de habilidades
#   4. Algoritmo Genético (AG) completo
# =============================================================================


import random
from collections import deque

# =============================================================================
# 0. DADOS DO PROBLEMA
# =============================================================================

# Cada pessoa é um dicionário com:
#   nome        -> identificador
#   habilidades -> conjunto de skills que ela possui
#   custo       -> quanto custa incluí-la no time (ex.: salário mensal)
#   performance -> pontuação de produtividade / qualidade esperada

PESSOAS = [
    {"nome": "Alice",  "habilidades": {"Python", "Machine Learn"}, "custo": 5000, "performance": 9},
    {"nome": "Bruno",  "habilidades": {"Java", "Backend"},         "custo": 4500, "performance": 8},
    {"nome": "Carla",  "habilidades": {"Frontend", "UX"},          "custo": 4000, "performance": 7},
    {"nome": "Diego",  "habilidades": {"DevOps", "Cloud"},         "custo": 5500, "performance": 9},
    {"nome": "Eva",    "habilidades": {"Python", "Data"},          "custo": 4800, "performance": 8},
    {"nome": "Fábio",  "habilidades": {"Backend", "Java"},         "custo": 3800, "performance": 6},
    {"nome": "Gabi",   "habilidades": {"Machine Learn", "Data"},   "custo": 5200, "performance": 9},
    {"nome": "Hugo",   "habilidades": {"Frontend", "Cloud"},       "custo": 4100, "performance": 7},
    {"nome": "Íris",   "habilidades": {"UX", "Frontend"},          "custo": 3500, "performance": 6},
    {"nome": "João",   "habilidades": {"DevOps", "Backend"},       "custo": 4700, "performance": 8},
]

# Habilidades que o projeto exige — o time precisa cobrir TODAS elas
HABILIDADES_NECESSARIAS = {"Python", "Machine Learn", "Frontend", "Backend", "DevOps"}

# Orçamento máximo disponível para o time
ORCAMENTO = 18000

N = len(PESSOAS)  # total de candidatos disponíveis

# =============================================================================
# 1. MODELAGEM COMO ESPAÇO DE ESTADOS
# =============================================================================
#
# Estado       -> tupla binária de tamanho N (0 = não incluído, 1 = incluído)
#                 Ex.: (1, 0, 1, 0, ...) significa que a pessoa 0 e a 2 estão no time.
#
# Estado Inicial -> todos zeros: ninguém selecionado ainda -> (0, 0, 0, ..., 0)
#
# Operadores   -> para cada pessoa ainda não avaliada, podemos INCLUÍ-LA ou
#                 EXCLUÍ-LA; na BFS modelamos isso como "adicionar a próxima
#                 pessoa" ao time parcial, gerando dois filhos por nó.
#
# Estado Objetivo -> um estado onde:
#   • custo total ≤ ORCAMENTO
#   • habilidades cobertas ⊇ HABILIDADES_NECESSARIAS
#   • queremos MAXIMIZAR a performance total do time

def custo_total(estado):
    # Soma os custos das pessoas incluídas no estado.
    return sum(PESSOAS[i]["custo"] for i, bit in enumerate(estado) if bit == 1)

def performance_total(estado):
    # Soma as performances das pessoas incluídas no estado.
    return sum(PESSOAS[i]["performance"] for i, bit in enumerate(estado) if bit == 1)

def habilidades_cobertas(estado):
    # Retorna o conjunto de habilidades cobertas pelo time representado pelo estado.
    skills = set()
    for i, bit in enumerate(estado):
        if bit == 1:
            skills |= PESSOAS[i]["habilidades"]
    return skills

def eh_objetivo(estado):
    
    # Um estado é OBJETIVO se:
    # - Não excede o orçamento
    # - Cobre todas as habilidades necessárias

    return (
        custo_total(estado) <= ORCAMENTO and
        HABILIDADES_NECESSARIAS.issubset(habilidades_cobertas(estado))
    )

# =============================================================================
# 2. HEURÍSTICA DE COBERTURA DE HABILIDADES
# =============================================================================
#
# Justificativa: em problemas de cobertura de conjuntos, uma boa heurística
# é medir QUANTAS habilidades ainda faltam ser cobertas. Quanto menor esse
# número, mais perto estamos de um time completo.
#
# h(estado) = |habilidades_necessárias − habilidades_cobertas(estado)|
#
# Essa heurística é admissível (nunca superestima) e serve para:
#   a) Podar ramos inviáveis na BFS
#   b) Compor o bônus da função fitness no AG

def heuristica(estado):
    """
    Retorna o número de habilidades que ainda faltam no time.
    h = 0 significa cobertura total (estado objetivo em termos de skills).
    Quanto menor, melhor.
    """
    faltando = HABILIDADES_NECESSARIAS - habilidades_cobertas(estado)
    return len(faltando)

# =============================================================================
# 3. BUSCA EM LARGURA (BFS)
# =============================================================================
#
# Exploramos o espaço de estados nível por nível.
# Cada nível corresponde a decidir sobre a i-ésima pessoa (incluir ou não).
# A BFS garante encontrar a solução com MENOR NÚMERO DE PESSOAS no time
# (menor profundidade), dentre todas as soluções válidas.
#
# Poda: descartamos ramos onde o custo já excede o orçamento antes de
# examinar todas as pessoas — evita explorar combinações inviáveis.

def bfs():

    # Realiza BFS no espaço de estados.
    # Retorna a MELHOR solução encontrada (maior performance), ou None.

    # Estado inicial: ninguém selecionado, e decidimos sobre a pessoa 0 em seguida.
    # Cada item na fila: (estado_parcial_como_lista, próximo_índice_a_decidir)
    fila = deque()
    fila.append(([0] * N, 0))  # estado inicial + índice da próxima pessoa

    melhor_estado = None
    melhor_performance = -1
    nos_explorados = 0

    while fila:
        estado_parcial, idx = fila.popleft()
        nos_explorados += 1

        # Se já decidimos sobre todas as pessoas, avaliamos o estado completo
        if idx == N:
            estado = tuple(estado_parcial)
            if eh_objetivo(estado):
                perf = performance_total(estado)
                if perf > melhor_performance:
                    melhor_performance = perf
                    melhor_estado = estado
            continue

        # Poda por custo: se já excedrmos o orçamento, este ramo é inviável
        if custo_total(tuple(estado_parcial)) > ORCAMENTO:
            continue

        # Poda heurística: se nem somando TODOS os candidatos restantes
        # conseguiríamos cobrir as habilidades, descartamos este ramo
        skills_possiveis = habilidades_cobertas(tuple(estado_parcial))
        for j in range(idx, N):
            skills_possiveis |= PESSOAS[j]["habilidades"]
        if not HABILIDADES_NECESSARIAS.issubset(skills_possiveis):
            continue

        # Geração dos dois filhos: NÃO incluir pessoa idx / INCLUIR pessoa idx
        for bit in (0, 1):
            novo_estado = estado_parcial[:]
            novo_estado[idx] = bit
            fila.append((novo_estado, idx + 1))

    print(f"[BFS] Nós explorados: {nos_explorados}")
    return melhor_estado

# =============================================================================
# 4. ALGORITMO GENÉTICO (AG)
# =============================================================================
#
# O AG explora o espaço de forma paralela (população de soluções) e guiada
# pela pressão seletiva, sendo ideal quando o espaço é grande demais para BFS.
#
# == 4.1 Representação do Cromossomo =========================================
# Cromossomo = lista binária de tamanho N
# Gene i = 1 -> pessoa i incluída no time | Gene i = 0 -> excluída
# Ex.: [1, 0, 0, 1, 1, 0, 0, 1, 0, 0]
#
# == 4.2 Função Fitness ======================================================
# Queremos MAXIMIZAR: performance total com bônus por cobertura de habilidades
# Penalizamos: extrapolação do orçamento
#
# fitness = performance_total
#           + 10 * habilidades_necessárias_cobertas
#           - penalidade por excesso de custo
#
# == 4.3 Seleção: Torneio ====================================================
# Sorteamos k indivíduos e o de maior fitness vence — mantém diversidade.
#
# == 4.4 Crossover: Um Ponto =================================================
# Ponto aleatório divide os dois pais; filhos trocam os segmentos.
#
# == 4.5 Mutação: Flip de Bit ================================================
# Com probabilidade taxa_mutacao, cada gene é invertido (0 -> 1 ou 1 -> 0).

# == Parâmetros do AG =========================================================
TAM_POPULACAO  = 80    # número de indivíduos na população
NUM_GERACOES   = 200   # quantidade de gerações
TAXA_CROSSOVER = 0.85  # probabilidade de realizar crossover
TAXA_MUTACAO   = 0.05  # probabilidade de mutar cada gene
TAM_TORNEIO    = 5     # tamanho do torneio de seleção
ELITISMO       = 2     # quantos melhores passam direto para a próxima geração


def gerar_individuo():
    # Cria um cromossomo aleatório (solução candidata).
    return [random.randint(0, 1) for _ in range(N)]


def pegar_fitness(indice, fitnesses):
    #Retorna o valor de fitness de um indivíduo pelo seu índice na lista.
    return fitnesses[indice]


def calcular_fitness(individuo):
    """
    Função fitness — avalia a qualidade do cromossomo.

    Componentes:
      + performance acumulada das pessoas selecionadas
      + 10 pontos por cada habilidade necessária coberta pelo time
      - penalidade proporcional se o custo exceder o orçamento
    """
    estado = tuple(individuo)
    perf   = performance_total(estado)
    custo  = custo_total(estado)
    skills = habilidades_cobertas(estado)

    # Bônus por cobertura de habilidades necessárias
    cobertas     = len(HABILIDADES_NECESSARIAS & skills)
    bonus_skills = cobertas * 10

    # Penalidade por excesso de orçamento (proporcional ao excesso)
    if custo > ORCAMENTO:
        penalidade = (custo - ORCAMENTO) / 100
    else:
        penalidade = 0

    return perf + bonus_skills - penalidade


def selecao_torneio(populacao, fitnesses):
    
    # Seleção por Torneio:
    # Sorteia TAM_TORNEIO indivíduos aleatoriamente e retorna o melhor.
    # Mantém pressão seletiva sem eliminar toda a diversidade.
    
    candidatos = random.sample(range(len(populacao)), TAM_TORNEIO)

    # Seleciona o candidato com maior fitness entre os sorteados
    def criterio_torneio(indice):
        return pegar_fitness(indice, fitnesses)

    vencedor = max(candidatos, key=criterio_torneio)
    return populacao[vencedor][:]  # retorna cópia do vencedor


def crossover_um_ponto(pai1, pai2):
    
    # Crossover de Um Ponto:
    # Um ponto de corte aleatório divide os pais em dois segmentos.
    # Os filhos recebem segmentos alternados de cada pai.
    
    if random.random() > TAXA_CROSSOVER:
        return pai1[:], pai2[:]  # sem crossover, filhos = cópias dos pais

    ponto  = random.randint(1, N - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2


def mutacao_flip_bit(individuo):
    
    # Mutação por Flip de Bit:
    # Cada gene tem TAXA_MUTACAO de chance de ser invertido (0 ↔ 1).
    # Garante diversidade genética e evita convergência prematura.
    
    return [1 - gene if random.random() < TAXA_MUTACAO else gene
            for gene in individuo]


def algoritmo_genetico():
    
    # Loop principal do Algoritmo Genético.
    # Retorna o melhor indivíduo encontrado após NUM_GERACOES gerações.
    
    # Inicialização: população totalmente aleatória
    populacao = [gerar_individuo() for _ in range(TAM_POPULACAO)]

    melhor_global = None
    melhor_fitness_global = -float("inf")

    for geracao in range(1, NUM_GERACOES + 1):

        # Avaliação: calcula o fitness de cada indivíduo da população
        fitnesses = [calcular_fitness(ind) for ind in populacao]

        # Elitismo: ordena a população do maior para o menor fitness
        # e preserva os ELITISMO melhores diretamente na próxima geração
        def criterio_ordenacao(indice):
            return pegar_fitness(indice, fitnesses)

        indices_ordenados = sorted(
            range(TAM_POPULACAO),
            key=criterio_ordenacao,
            reverse=True
        )
        elite = [populacao[i][:] for i in indices_ordenados[:ELITISMO]]

        # Atualiza o melhor indivíduo encontrado em toda a execução
        melhor_idx = indices_ordenados[0]
        if fitnesses[melhor_idx] > melhor_fitness_global:
            melhor_fitness_global = fitnesses[melhor_idx]
            melhor_global         = populacao[melhor_idx][:]

        # Reprodução: preenche a nova população via seleção, crossover e mutação
        nova_populacao = elite[:]  # elite passa direto para a próxima geração

        while len(nova_populacao) < TAM_POPULACAO:
            # Seleção: escolhe dois pais por torneio
            pai1 = selecao_torneio(populacao, fitnesses)
            pai2 = selecao_torneio(populacao, fitnesses)

            # Crossover: combina os pais para gerar dois filhos
            filho1, filho2 = crossover_um_ponto(pai1, pai2)

            # Mutação: aplica variações aleatórias nos filhos
            filho1 = mutacao_flip_bit(filho1)
            filho2 = mutacao_flip_bit(filho2)

            nova_populacao.append(filho1)
            if len(nova_populacao) < TAM_POPULACAO:
                nova_populacao.append(filho2)

        populacao = nova_populacao

        # Log a cada 50 gerações para acompanhar a evolução
        if geracao % 50 == 0 or geracao == 1:
            print(f"  [AG] Geração {geracao:3d} | Melhor fitness: {melhor_fitness_global:.2f}")

    return melhor_global


# =============================================================================
# 5. UTILITÁRIOS DE EXIBIÇÃO
# =============================================================================

def exibir_resultado(titulo, estado):
    # Imprime um resumo formatado do time selecionado.
    if estado is None:
        print(f"\n{'='*60}")
        print(f"  {titulo}")
        print(f"  Nenhuma solução válida encontrada.")
        print(f"{'='*60}\n")
        return

    estado_t         = tuple(estado)
    time_selecionado = [PESSOAS[i] for i, bit in enumerate(estado_t) if bit == 1]

    print(f"\n{'='*60}")
    print(f"  {titulo}")
    print(f"{'='*60}")
    print(f"  Time selecionado ({len(time_selecionado)} pessoa(s)):")
    for p in time_selecionado:
        print(f"    • {p['nome']:8s} | Custo: R${p['custo']:,} "
              f"| Perf: {p['performance']} "
              f"| Skills: {', '.join(sorted(p['habilidades']))}")

    print(f"\n  Custo total  : R${custo_total(estado_t):,} / R${ORCAMENTO:,}")
    print(f"  Performance  : {performance_total(estado_t)}")
    print(f"  Skills cob.  : {', '.join(sorted(habilidades_cobertas(estado_t)))}")

    faltando = HABILIDADES_NECESSARIAS - habilidades_cobertas(estado_t)
    if faltando:
        print(f"  ⚠ Habilidades faltando: {', '.join(sorted(faltando))}")
    else:
        print(f"  ✔ Todas as habilidades cobertas!")

    valido = eh_objetivo(estado_t)
    print(f"  Solução válida: {'✔ Sim' if valido else '✗ Não'}")
    print(f"{'='*60}\n")


# =============================================================================
# 6. EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == "__main__":

    print("\n" + "="*60)
    print("  MONTAGEM DE TIME DE PROJETO")
    print("  Orçamento:", f"R${ORCAMENTO:,}")
    print("  Habilidades necessárias:", ", ".join(sorted(HABILIDADES_NECESSARIAS)))
    print("  Candidatos disponíveis:", N)
    print("="*60)

    # Demonstração da heurística sobre o estado inicial e um exemplo parcial
    print("\n[HEURÍSTICA] Avaliação do estado inicial (ninguém selecionado):")
    estado_inicial = tuple([0] * N)
    print(f"  h(estado_inicial) = {heuristica(estado_inicial)} habilidades faltando")

    estado_ex = tuple([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(f"\n[HEURÍSTICA] Com apenas Alice no time:")
    print(f"  Skills cobertas : {habilidades_cobertas(estado_ex)}")
    print(f"  h(estado)       = {heuristica(estado_ex)} habilidade(s) faltando")

    # BFS
    print("\n" + "-"*60)
    print("  BUSCA EM LARGURA (BFS)")
    print("-"*60)
    resultado_bfs = bfs()
    exibir_resultado("Melhor solução encontrada pela BFS", resultado_bfs)

    # Algoritmo Genético
    print("-"*60)
    print("  ALGORITMO GENÉTICO (AG)")
    print("-"*60)
    print(f"  Parâmetros: pop={TAM_POPULACAO}, gerações={NUM_GERACOES}, "
          f"crossover={TAXA_CROSSOVER}, mutação={TAXA_MUTACAO}\n")

    random.seed(42)  # semente fixa para reprodutibilidade dos resultados
    resultado_ag = algoritmo_genetico()
    exibir_resultado("Melhor solução encontrada pelo AG", resultado_ag)

    # Comparação final
    print("="*60)
    print("  COMPARAÇÃO BFS vs AG")
    print("="*60)

    def resumo(nome, estado):
        if estado is None:
            print(f"  {nome:5s}: sem solução válida")
            return
        t      = tuple(estado)
        valido = eh_objetivo(t)
        print(f"  {nome:5s}: performance={performance_total(t):3d} | "
              f"custo=R${custo_total(t):,} | "
              f"válido={'✔' if valido else '✗'} | "
              f"habilidades faltando={heuristica(t)}")

    resumo("BFS", resultado_bfs)
    resumo("AG ", resultado_ag)
    print("="*60 + "\n")