rendaMensal = float(input("Insira sua renda mensal: "))
scoreCredito = float(input("Insira seu score: "))
restricao = input("Possui restrição ?(sim/não) ").lower()

def CalculaRiscoCredito():
    if(scoreCredito > 700 and restricao == "n"):
        print("Aprovado")
    elif(scoreCredito <= 700 and scoreCredito >= 500):
        print("Análise Manual")
    else:
        print("NEGADO")

CalculaRiscoCredito()