from collections import deque

def executar_entregador(grafo, inicio):
    fila = deque((inicio))
    visitados = set([inicio])
    print("\n === INICIANDO BFS (VARREDURA POR NIVEL) ===")

    while fila:
        local_atual = fila.popleft()
        print(f"Entregando em: {local_atual}")

        for vizinho in grafo[local_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    print("=============================================")
    print("\n" + "="*10)

def executar_dfs_software(grafo, etapa, rastro = None):
    if rastro is None:
        rastro = []
        rastro.append(etapa)
        print(f"Analisando a trilha: {'=>'.join(rastro)}")
        
        if not grafo[etapa]:
            print(f"SUCESSO! Objetivo encontrado no fim da linha: {etapa}")
        return True
    
    for proximo in grafo[etapa]:
        if executar_dfs_software(grafo, proximo, list(rastro)):
            return True
    return False

mapa_entrega = {
    'CD Logistico': ['Rua A', 'Rua B', "Rua C"],
    'Rua A': ['Casa 1'],
    'Rua B': [],
    'Rua C': [],
    'Casa 1': []
}

mapa_software = {
    'Nova Ideia':['N8N', 'Código'],
    'n8n':['Criar os nós'],
    'Código':['Configurar NextJS'],
    'Criar os nós': [],
    'Configurar NextJS': []
}

if __name__ == "__main__":
    executar_entregador(mapa_entrega, "CD Logistico")
    print("\n" + "=" *10)
    print("\n === INICIANDO DFS (MERGULHO PROFUNDO) ===")
    executar_dfs_software(mapa_software, 'Nova Ideia')