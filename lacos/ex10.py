populacao_a = 1000
populacao_b = 5000
anos = 0

while populacao_a <= populacao_b:
    populacao_a = populacao_a * 1.03
    populacao_b = populacao_b * 1.015
    anos += 1

print(f"Anos para A ultrapassar B: {anos}")
print(f"População final de A: {populacao_a:.2f}")
print(f"População final de B: {populacao_b:.2f}")
