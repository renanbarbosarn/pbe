tempo = float(input("Tempo para impressão da peça (em minutos): "))
quantidadeProduzida = int(input("Quantidade produzida de peças: "))

quant_em_hora = quantidadeProduzida * tempo / 60

print(f"Tempo de produção em horas: {quant_em_hora}")
