import numpy as np

dados = []

for linha in range(3):
    linha_matriz = []
    for coluna in range(3):
        valor = int(input(f"Digite o valor para [{linha}][{coluna}]: "))
        linha_matriz.append(valor)
    dados.append(linha_matriz)

matriz = np.array(dados)

soma_total = matriz.sum()
maior_valor = matriz.max()
soma_diagonal = matriz.trace()
quantidade_pares = (matriz % 2 == 0).sum()

print()
print("Matriz:")
print(matriz)
print(f"Soma de todos os elementos: {soma_total}")
print(f"Maior valor: {maior_valor}")
print(f"Soma da diagonal principal: {soma_diagonal}")
print(f"Quantidade de números pares: {quantidade_pares}")
