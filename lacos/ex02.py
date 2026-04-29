n = int(input("Digite um número inteiro positivo: "))

while n <= 0:
    print("Valor inválido. Digite um número inteiro positivo.")
    n = int(input("Digite um número inteiro positivo: "))

iteracoes = 0
maior_numero = n

print("Sequência de Collatz:")
print(n)

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    print(n)
    iteracoes += 1

    if n > maior_numero:
        maior_numero = n

print(f"Total de iterações: {iteracoes}")
print(f"Maior número atingido: {maior_numero}")
