soma = 0
termos = 0
n = 1

parcela = 1 / n

while parcela >= 0.001:
    soma = soma + parcela
    termos = termos + 1
    n = n + 1
    parcela = 1 / n

print(f"Quantidade de termos: {termos}")
print(f"Soma final: {soma}")
