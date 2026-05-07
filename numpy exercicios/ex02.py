import numpy as np

matriz = np.random.randint(-10, 11, size=(3, 3))

print("Matriz original:")
print(matriz)

soma_principal = np.trace(matriz)

soma_secundaria = np.trace(np.fliplr(matriz))

print(f"Soma da diagonal principal: {soma_principal}")
print(f"Soma da diagonal secundária: {soma_secundaria}")

matriz_filtrada = np.where(matriz < 0, 0, matriz)

print("Matriz após filtragem (negativos substituídos por zero):")
print(matriz_filtrada)
