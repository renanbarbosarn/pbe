votos_1 = 0
votos_2 = 0
votos_3 = 0
votos_nulos = 0

print("Eleição: vote em 1, 2 ou 3. Digite 0 para encerrar.")

voto = int(input("Digite seu voto: "))

while voto != 0:
    if voto == 1:
        votos_1 += 1
    elif voto == 2:
        votos_2 += 1
    elif voto == 3:
        votos_3 += 1
    else:
        votos_nulos += 1

    voto = int(input("Digite seu voto: "))

total_votos = votos_1 + votos_2 + votos_3 + votos_nulos

if total_votos > 0:
    porcentagem_1 = (votos_1 / total_votos) * 100
    porcentagem_2 = (votos_2 / total_votos) * 100
    porcentagem_3 = (votos_3 / total_votos) * 100
    porcentagem_nulos = (votos_nulos / total_votos) * 100
else:
    porcentagem_1 = 0
    porcentagem_2 = 0
    porcentagem_3 = 0
    porcentagem_nulos = 0

print(f"Total de votos: {total_votos}")
print(f"Candidato 1: {votos_1} voto(s) - {porcentagem_1:.2f}%")
print(f"Candidato 2: {votos_2} voto(s) - {porcentagem_2:.2f}%")
print(f"Candidato 3: {votos_3} voto(s) - {porcentagem_3:.2f}%")
print(f"Nulos: {votos_nulos} voto(s) - {porcentagem_nulos:.2f}%")

if votos_1 > votos_2 and votos_1 > votos_3:
    print("Vencedor: Candidato 1")
elif votos_2 > votos_1 and votos_2 > votos_3:
    print("Vencedor: Candidato 2")
elif votos_3 > votos_1 and votos_3 > votos_2:
    print("Vencedor: Candidato 3")
elif total_votos == 0:
    print("Sem votos para definir vencedor.")
else:
    print("Empate entre candidatos.")
