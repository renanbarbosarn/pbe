numero = int(input("Digite um número inteiro positivo: "))

while numero <= 0:
    print("Valor inválido. Digite um número inteiro positivo.")
    numero = int(input("Digite um número inteiro positivo: "))

soma_divisores = 0
divisores_texto = ""

for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

        if divisores_texto == "":
            divisores_texto = str(i)
        else:
            divisores_texto = divisores_texto + " + " + str(i)

print(f"Divisores (exceto ele): {divisores_texto}")
print(f"Soma dos divisores: {soma_divisores}")

if soma_divisores == numero:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")
