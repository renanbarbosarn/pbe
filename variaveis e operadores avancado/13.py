tam_log = float(input("Qual o tamanho médio do log em MB? "))
qtd_logs = int(input("Quantos logs são gerados por dia? "))

total_mb = tam_log * qtd_logs

print(f"O tamanho total de logs no dia foi de {total_mb:.2f} MB")
