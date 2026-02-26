import numpy as np

def Alunos():
    for t in range(1, 11):
        fatorE = np.random.randint(0, 21, size=10)   # tempo de estudo
        fatorF = np.random.randint(0, 16, size=1)   # dias de falta
        media = np.mean(fatorE)
        desvio = np.std(fatorE)
        i = (fatorE * 0.6) - (fatorF * 0.4)# cálculo de indice
        iap = np.mean(i) #Média de indice de aproveitamento padrão 

        if(iap >= 7.0):
            dgn = "Alta chance de aprovação"
        elif(iap >= 5.0 and iap < 7.0):
            dgn = "Risco moderado de reprovação"
        else:
            dgn = "Intervenção Imediata"

        print(f"\n====================== Base de Dados =====================")
        print(f"Aluno: {t}")
        print(f"FatorE (tempo de estudo): {fatorE}")
        print(f"FatorF (dias de falta):   {fatorF}")
        print(f"\nMédia de tempo investido: {media:.2f} horas")
        print(f"Desvio padrão:            {desvio:.2f} horas")
        print(f"IAP: {iap}")
        print(f"Diagnóstico Final: {dgn}")
        print(f"==========================================================\n")

Alunos()
