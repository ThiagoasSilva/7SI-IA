### 1.  Pela sua análise, o que é o fator E e o fator A? 

O Fator E representa o engajamento acadêmico do aluno o quanto ele investe tempo estudando. Imaginando que Fator A seja o Fator F, ele representa a frequência de faltas, os dias em que o aluno esteve ausente.

### 2.  Olhando para os resultados, você acha que o modelo parece realista? Essa conta é justa com quem falta pouco, mas estuda muito? 

Acredito que parcialmente. O modelo percebe que estudar muito pode compensar algumas faltas. No entanto, ele ignora completamente variáveis importantes como dificuldade do conteúdo, qualidade do estudo, desempenho em provas. Um aluno que falta por motivos de saúde mas estuda em casa recebe o mesmo tratamento que um que simplesmente não aparece, o modelo não distingue o motivo da falta. Então é uma aproximação útil, mas não justa ou completa.

### 3.  Para que um computador aprenda a prever essas notas sozinho (sem você dar a fórmula), o que ele precisaria receber além desses dados? 

Para que um modelo de Machine Learning aprendesse essa relação sem receber a fórmula, ele precisaria de:

- Dados históricos rotulados: registros de alunos anteriores com seus valores de Fator E, Fator F e o resultado real.

- Um alvo claro: a variável que ele deve prever como a nota final ou o diagnóstico
Volume suficiente de exemplos onde quanto mais alunos no histórico, melhor o aprendizado

- Possivelmente mais variáveis: notas de provas, participação em aula, histórico anterior, para que o modelo encontre padrões mais ricos do que os dois fatores atuais permitem