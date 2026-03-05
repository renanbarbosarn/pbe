import math

print("Informe o número da posição de x e y no plano cartesiano.")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distancia_euclidiana = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"A distância entre esses dois pontos no plano cartesiano é de: {distancia_euclidiana}")
