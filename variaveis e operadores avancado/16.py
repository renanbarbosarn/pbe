watts = float(input("Qual o consumo de cada servidor em watts? "))
qtd = int(input("Quantos servidores tem no total? "))

total_watts = watts * qtd

print(f"O consumo total de energia do data center é de {total_watts:.2f} watts")
