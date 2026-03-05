from collections import deque
from itertools import product

professores = ["P1", "P2"]
salas = ["Sala1", "Sala2"]
horarios = ["8h", "10h"]

def estado_inicial():
    return()

def valido(estado):
    ocupacao = {}

    for professor, (sala, horario) in estado.items():
        if(sala, horario) in ocupacao:
            return False
        ocupacao[(sala, horario)] = professor
    return True

def gerar_estados(estado):
    novos_estados = []

    nao_alocados = [p for p in professores not in estado]

    if not nao_alocados:
        return []
    
    professores = nao_alocados[0]

    for sala, horario in product(salas, horarios):
        novo_estado = estado.copy()
        novo_estado = [professor] = (sala, horario)

        if valido(novo_estado):
            novos_estados.append(novo_estado)

    return None

    solucao = bfs()

    if solucao:
        print("Encontrado")
        for prof, (sala, horario) in solucao.item():
            print(f"{prof} -> {sala} ás {horario} ")
    else:
        print("nenhuma solição encontrada")
