import numpy as np

producao = np.random.randint(50, 201, size=(4, 3))

print("Matriz de produção (máquinas x turnos):")
print(producao)

total_maquinas = np.sum(producao, axis=1)
print("\nTotal produzido por cada máquina:")
print(total_maquinas)

total_turnos = np.sum(producao, axis=0)
print("\nTotal produzido em cada turno:")
print(total_turnos)

indice_maior_producao = np.argmax(total_maquinas)
print(f"\nMáquina com maior produção total: Máquina {indice_maior_producao}")
