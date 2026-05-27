# 🎓 Inteligência Artificial - 7º Semestre (Sistemas de Informação)
> **UniProjeção**  
> Repositório destinado ao armazenamento, versionamento e documentação de práticas, algoritmos e exercícios práticos desenvolvidos na disciplina de **Inteligência Artificial (IA)**.

---

## 📁 Estrutura de Diretórios e Resumos de Conteúdo

Abaixo está o mapeamento dos módulos práticos do repositório, detalhando o propósito de cada algoritmo e arquivo de configuração versionado.

---

### 📊 Aula 02: Reapresentação, Python & Análise Estatística
*Foco: Introdução à sintaxe do Python e modelagem de modelos estatísticos preditivos.*

*   **Diretório: `A02_Reapresentacao-e-ambientacao_230226/`**
    *   `estatisticaBasica.py`: Script Python básico que recebe amostragem de dados e extrai métricas como quantidade, valor máximo, mínimo, média e desvio simples.
    *   `programaAluno.py`: Lógica condicional para cálculo de médias escolares e diagnóstico de aprovação acadêmica.
    *   `simuaClassificador.py`: Simulador de classificação de risco de crédito com regras de decisão estruturadas (score de crédito e presença de restrições financeiras).
    *   `Exercicio1-analiseEstatiscica-modeloPrevisao/`: 
        *   `Exercicio1.md`: Descrição do problema para modelagem do Índice de Aproveitamento (IAp) de alunos.
        *   `ex1.py`: Resolução prática em Python gerando arrays aleatórios no `NumPy`, calculando o IAp e diagnosticando o perfil do grupo.
        *   `ex1-respostas.md`: Respostas e análise crítica sobre as limitações do modelo preditivo formulado e os requisitos necessários para a transição para Machine Learning (dados históricos rotulados, targets claros e novos atributos).

---

### 🗺️ Aula 03: Espaço de Estados & Busca em Largura (BFS)
*Foco: Modelagem matemática de problemas e algoritmos de busca cega aplicados a restrições reais de agendamento.*

*   **Diretório: `A03_modelagem-de-problemas_040326/`**
    *   `salas.py`: Algoritmo básico de alocação de salas e horários de professores, validando conflitos de agenda no espaço de estados.
    *   `exercicio02/Exercicio02.py`: Algoritmo prático de Busca em Largura (BFS) implementado com `collections.deque` que resolve de forma ótima o problema de alocação de escala de monitores em laboratórios de informática, atendendo a restrições como horários bloqueados e preferências específicas de salas.
    *   `exercicio02/guia02.md`: Guia documentado contendo as restrições e regras de negócio utilizadas na construção da lógica de busca do algoritmo.

---

### 🤿 Aula 04: Busca em Profundidade (DFS) & Varredura Lógica
*Foco: Comparação do comportamento entre Busca em Largura (BFS - FIFO por nível) e Busca em Profundidade (DFS - LIFO recursiva).*

*   **Diretório: `A04_dfs_110326/`**
    *   `ex.py`: Script comparativo implementando os dois principais algoritmos de busca cega:
        *   **Busca em Largura (BFS)**: Simulador de entregas que varre o grafo (`mapa_entrega`) expandindo por nível a partir de um Centro de Distribuição Central.
        *   **Busca em Profundidade (DFS)**: Script recursivo que executa uma árvore de dependências lógicas para o desenvolvimento de módulos de software (`mapa_software`), priorizando o aprofundamento das ramificações até encontrar o objetivo.

---

### 🧬 Aula 05: Heurísticas & Algoritmo Genético (AG I)
*Foco: Introdução à inteligência evolucionária e algoritmos de otimização populacional.*

*   **Diretório: `A05_algoritmo-genetico_180326/`**
    *   `euristica.py`: Implementação prática de um **Algoritmo Genético (AG)** básico. O programa inicializa e evolui uma população de vetores binários representando características de posts em redes sociais (ex: Vídeo Curto, Legenda Embutida, Áudio Viral, etc.). Utiliza operadores de aptidão (*fitness*), cruzamento (*crossover*) e mutação para encontrar, através de ciclos evolutivos, o arranjo perfeito de engajamento (fitness máximo de 20 pontos).

---

### 📈 Aula 06: Algoritmos Genéticos de Otimização (AG II)
*Foco: Aplicação corporativa de algoritmos evolucionários em problemas de otimização de recursos financeiros.*

*   **Diretório: `A06_marketing_250326/`**
    *   `marketing.py`: Algoritmo Genético de nível corporativo desenvolvido para otimizar a distribuição de uma verba de R$ 10.000,00 entre 4 canais de anúncios (Google, Meta, Tiktok, Youtube). O algoritmo calcula o retorno total utilizando curvas de saturação e valores de ROAS específicos para cada canal. Roda seleções, cruzamentos com balanceamento e mutações por remanejamento para encontrar a alocação de verba evolutiva que traga o retorno financeiro máximo.

---

### 🤖 Aula 07: Agentes Inteligentes, Chatbots & n8n
*Foco: Integração de fluxos de dados, IA conversacional e automação de serviços.*

*   **Diretório: `A07_chatbot_010426/`**
    *   `docker-compose.yml`: Definição de contêineres Docker para inicialização local de microsserviços de apoio aos fluxos.
    *   `upj-ia.json`: Configurações de fluxos de integração exportadas do **n8n** (ferramenta de automação baseada em nós), estruturando canais de diálogo inteligente para chatbots.
    *   `n8nac-config.json` (raiz do repositório): Arquivo de configuração de sincronização para conexões ativas com servidores e instâncias do n8n.

---

## 🛠️ Tecnologias e Configuração do Ambiente

Para executar os scripts práticos de IA contidos no repositório:

### 1. Requisitos do Sistema
*   **Python 3.8+** instalado.
*   **Pip** (gerenciador de pacotes do Python).
*   **Docker & Docker Compose** (opcional, necessário apenas para os serviços da aula 07).

### 2. Instalação de Dependências
A maior parte dos scripts consome recursos nativos do Python, mas a análise estatística de matrizes na Aula 02 consome pacotes matemáticos do `NumPy`. Para instalá-los:
```bash
pip install numpy
```

### 3. Como Executar os Algoritmos Principais

*   **Executar a Busca BFS (Alocação de Monitores - Aula 03):**
    ```bash
    python A03_modelagem-de-problemas_040326/exercicio02/Exercicio02.py
    ```

*   **Executar a Comparação BFS vs. DFS (Aula 04):**
    ```bash
    python A04_dfs_110326/ex.py
    ```

*   **Executar o Algoritmo Genético de Otimização de Posts (Aula 05):**
    ```bash
    python A05_algoritmo-genetico_180326/euristica.py
    ```

*   **Executar a Otimização Genética de Verba de Marketing (Aula 06):**
    ```bash
    python A06_marketing_250326/marketing.py
    ```
