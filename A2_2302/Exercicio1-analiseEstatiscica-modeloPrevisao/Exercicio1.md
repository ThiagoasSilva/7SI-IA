# EXERCÍCIO 1: ANÁLISE ESTATÍSTICA + MODELO DE PREVISÃO 
### DATA ENTREGA: 25/02 

Neste exercício, você vai atuar como o analista de dados da disciplina de IA. Siga os 
passos para gerar os dados, processar a planilha de desempenho e prever quem tem 
probabilidade de reprovar, ou de ser aprovado na disciplina. 
 
### Parte 1: Base de Dados 

Imagine que você tem 10 registros. Cada registro possui: 

- Fator E: Quantidade de tempo investido nos livros (entre 0 e 20). 
- Fator F: Quantidade de dias em que o aluno não compareceu (máximo 15). 

Gere esses dados usando NumPy. Em seguida, mostre para a coordenação qual é a 
média de investimento de tempo do grupo e o quanto esse grupo varia (desvio 
padrão) em relação ao tempo de estudo. 
 
### Parte 2: O Cálculo do Índice 
A nota final não é uma soma simples. Calcule o Índice de Aproveitamento (IAp) 
seguindo esta regra: 

Cada unidade do Fator E contribui com 60% de um ponto, enquanto cada unidade do 
Fator F penaliza o aluno em 40% de um ponto. 

~~~ bash
#Dica: 
I = (E * 0.6) - (F * 0.4) 
~~~
 
### Parte 3: Diagnóstico Final 
Com base no IAp calculado, apresente uma lista com o nome do aluno (pode ser 
"Aluno 1", "Aluno 2"...) e seu diagnóstico: 

- Se o IAp for pelo menos 7, o diagnóstico é " Alta chance de aprovação". 
- Se o IAp estiver entre 5 e 7, o diagnóstico é " Risco moderado de 
reprovação". 
- Se o IAp for menor que 5, o diagnóstico é "Intervenção Imediata". 
 
### Parte 4: Análise Crítica 
1.  Pela sua análise, o que é o fator E e o fator A? 

2.  Olhando para os resultados, você acha que o modelo parece realista? Essa 
conta é justa com quem falta pouco, mas estuda muito? 

3.  Para que um computador aprenda a prever essas notas sozinho (sem você dar a 
fórmula), o que ele precisaria receber além desses dados? 
 
### Parte 5: Entrega 
1.  Envie PDF contendo o código da solução e as respostas da Parte 4 a 
data limite. 

2.  O exercício deverá ser entregue pelo blog ou pelos e-mails que estão no 
cabeçalho. Enviar com cópia para os dois e-mails. 
  
`Bom trabalho! `
 
Prof. Kennto 
 
 
 
 
 
 
 
 
 
 