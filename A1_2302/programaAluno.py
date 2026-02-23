nomeaAluno = input("Digite o nome do aluno: ")

# Inserindo com float po rpadrão para declaração global
n1 = float(input("Digite a primeira n do aluno: "))
n2 = float(input("Digite a segunda n do aluno: "))
n3 = float(input("Digite a terceira n do aluno: "))

# convertendo após a inserção de string casodas notas caso possa ser reaproveitado se não como float
# n1 = input("Digite a primeira n do aluno: ")
# n2 = input("Digite a segunda n do aluno: ")
# n3 = input("Digite a terceira n do aluno: ")
# media = float(n1), float(n2), float(n3)

def CalculaNota():
    media = (n1 + n2 + n3) / 3
    if(media >= 7):
        print(f"O aluno {nomeaAluno} foi aprovado com a média: {round(media)}")
    elif(media >= 5) or (media < 7 ):
        print(f"O aluno {nomeaAluno} ficou de recuperação com a média: {round(media)}")
    else:        
        print(f"O aluno {nomeaAluno} foi reprovado com a média: {round(media)}")

CalculaNota()