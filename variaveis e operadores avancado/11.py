tempo_seg = float(input("Qual o tempo de uma tarefa em segundos? "))
qtd = int(input("Quantas tarefas foram executadas? "))

total_min = (tempo_seg * qtd) / 60

print(f"O tempo total de execução foi de {total_min:.2f} minutos")
