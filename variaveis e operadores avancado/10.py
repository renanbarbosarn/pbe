mensalidade = float(input("Qual o valor mensal do servidor? "))
meses = int(input("Quantos meses você contratou? "))

total = mensalidade * meses

print(f"O valor total pago pelo serviço foi de R$ {total:.2f}")
