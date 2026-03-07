from collections import deque
from itertools import product

monitores = ["M1", "M2", "M3"]
labs      = ["Lab1", "Lab2"]
horarios  = ["14h", "16h"]

def estado_inicial():
    return {}

def valido(estado):
    ocupacao = {}
    for monitor, (sala, horario) in estado.items():
    
        if monitor == "M1" and horario == "16h":
            return False
    
        if monitor == "M3" and sala != "Lab2":
            return False
    
        chave = (sala, horario)
        if chave in ocupacao:
            return False
        ocupacao[chave] = monitor
    return True

def gerar_estados(estado):
    novos_estados = []


    nao_alocados = [m for m in monitores if m not in estado]
    if not nao_alocados:
        return [] 

    proximo = nao_alocados[0]

    for sala, horario in product(labs, horarios):
        novo_estado = dict(estado)           
        novo_estado[proximo] = (sala, horario)

        if valido(novo_estado):              
            novos_estados.append(novo_estado)

    return novos_estados

def bfs():
    fila = deque()
    fila.append(estado_inicial())

    while fila:
        estado_atual = fila.popleft()

    
        if len(estado_atual) == len(monitores):
            return estado_atual

        for filho in gerar_estados(estado_atual):
            fila.append(filho)

    return None 

solucao = bfs()

if solucao:
    print("Solução encontrada:")
    for monitor, (sala, horario) in solucao.items():
        print(f"  {monitor} -> {sala} às {horario}")
else:
    print("Nenhuma solução encontrada.")