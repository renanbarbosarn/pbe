velocidade_internet = float(input("Digite a velocidade (Mbps): "))
tempo = int(input("Digite o tempo (segundos): "))
total_megabits = velocidade_internet * tempo
print(f"Total transferido: {total_megabits} megabits")
