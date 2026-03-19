import math

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

equilatero = a == b == c
print(f"Equilátero: {equilatero}")

isosceles = a == b or a == c or b == c
print(f"Isósceles: {isosceles}")

escaleno = a != b and a != c and b != c
print(f"Escaleno: {escaleno}")

p = (a + b + c) / 2

area = math.sqrt(p * (p-a) * (p-b) * (p-c))
print(f"Área do triângulo: {area:.2f}")
