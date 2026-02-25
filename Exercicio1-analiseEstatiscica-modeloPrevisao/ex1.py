import numpy as np

def dadosAluno():
    fatorE = np.random.randint(0, 21, size=10)   # tempo de estudo
    fatorF = np.random.randint(0, 16, size=1)   # dias de falta
    media = np.mean(fatorE)
    desvio = np.std(fatorE)

    for i in range(0, 11):
        print(f"\nAluno: {i}")
        print(f"FatorE (tempo de estudo): {fatorE}")
        print(f"FatorF (dias de falta):   {fatorF}")
        print(f"\nMédia de tempo investido: {media:.2f} horas")
        print(f"Desvio padrão:            {desvio:.2f} horas")
        print(f"==========================================================\n")
    
dadosAluno()