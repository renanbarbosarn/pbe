import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Tente adivinhar o número entre 1 e 100.")

while tentativas < 10 and acertou == False:
    palpite = int(input("Digite seu palpite: "))
    tentativas = tentativas + 1

    if palpite == numero_secreto:
        acertou = True
        print("Parabéns! Você acertou.")
    elif palpite > numero_secreto:
        diferenca = palpite - numero_secreto
        if diferenca > 20:
            print("Muito alto")
        else:
            print("Alto")
    else:
        diferenca = numero_secreto - palpite
        if diferenca > 20:
            print("Muito baixo")
        else:
            print("Baixo")

if acertou == False:
    print("Você atingiu o limite de 10 tentativas.")
    print(f"O número era: {numero_secreto}")

print(f"Número de tentativas: {tentativas}")
