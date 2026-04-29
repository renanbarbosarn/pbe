continuar = "s"

while continuar == "s":
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))

    while numero < 0:
        print("Número inválido. Não aceitamos negativos.")
        numero = int(input("Digite um número inteiro para calcular o fatorial: "))

    fatorial = 1
    contador = numero
    passo_a_passo = ""

    if numero == 0:
        passo_a_passo = "0! = 1"
    else:
        while contador >= 1:
            fatorial = fatorial * contador

            if passo_a_passo == "":
                passo_a_passo = str(contador)
            else:
                passo_a_passo = passo_a_passo + " x " + str(contador)

            contador = contador - 1

        passo_a_passo = str(numero) + "! = " + passo_a_passo + " = " + str(fatorial)

    print(f"Passo a passo: {passo_a_passo}")
    print(f"Resultado: {fatorial}")

    continuar = input("Deseja calcular outro fatorial? (s/n): ").lower()
