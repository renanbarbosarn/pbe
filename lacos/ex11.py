import time

n = int(input("Digite um número inteiro N: "))

while n < 2:
    print("Valor inválido. Digite um número inteiro maior ou igual a 2.")
    n = int(input("Digite um número inteiro N: "))

inicio_tempo = time.time()

marcado = [False] * (n + 1)
primos = []

for numero in range(2, n + 1):
    if marcado[numero] == False:
        primos.append(numero)

        multiplo = numero * 2
        while multiplo <= n:
            marcado[multiplo] = True
            multiplo += numero

fim_tempo = time.time()
tempo_execucao = fim_tempo - inicio_tempo

print(f"Primos até {n}: {primos}")
print(f"Quantidade total de primos: {len(primos)}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
