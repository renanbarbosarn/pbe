inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

while inicio >= fim:
    print("Intervalo inválido. O início deve ser menor que o fim.")
    inicio = int(input("Digite o início do intervalo: "))
    fim = int(input("Digite o fim do intervalo: "))

quantidade_primos = 0

print("Números primos no intervalo:")

for n in range(inicio, fim + 1):
    if n < 2:
        continue

    primo = True
    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            primo = False
            break
        divisor += 1

    if primo:
        print(n)
        quantidade_primos += 1

print(f"Total de primos encontrados: {quantidade_primos}")
