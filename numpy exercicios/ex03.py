import numpy as np

dados = np.random.randint(1, 101, size=10)

print("Vetor original:")
print(dados)

x_min = np.min(dados)
x_max = np.max(dados)
normalizado = (dados - x_min) / (x_max - x_min)

print("Vetor normalizado (Min-Max):")
print(normalizado)
