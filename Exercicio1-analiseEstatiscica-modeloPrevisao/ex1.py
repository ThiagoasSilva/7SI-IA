import numpy as np

fatorE = np.random.randint(0, 21, size=10)   # tempo de estudo
fatorF = np.random.randint(1, 16, size=10)   # dias de falta

media = np.mean(fatorE)
desvio = np.std(fatorE)

print("Fator E (tempo de estudo):", fatorE)
print("Fator F (dias de falta):  ", fatorF)
print(f"\nMédia de tempo investido: {media:.2f} horas")
print(f"Desvio padrão:            {desvio:.2f} horas")