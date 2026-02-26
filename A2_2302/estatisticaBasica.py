alturas = [
    1.65, 1.98, 1.54, 1.87, 1.71, 
    1.67, 1.70, 1.60, 1.75, 1.82, 
    1.59, 1.90, 1.68, 1.77, 1.85, 
    1.62, 1.73, 1.80, 1.55, 1.69
]

#QTD
print(f" Quantidade: {(len(alturas))}")

#MAX
print(f" Maior altura: {(max(alturas))}")

#MIN
print(f" Menor altura: {(min(alturas))}")

#MEDIA
def mediaAltura():
    mediaAlturas = sum(alturas) / len(alturas)
    print(f" Média: {mediaAlturas:.2f}")

mediaAltura()

#Desvio simples
def DesvioSimples():
    desvioSimples = max(alturas) - min(alturas)
    print(f"Desvio Simples: {desvioSimples}")

DesvioSimples()