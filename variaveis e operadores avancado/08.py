qtd = int(input("Quantas câmeras? "))
preco = float(input("Preço de cada câmera? "))
custo_inst = float(input("Custo de instalação por câmera? "))

total = qtd * (preco + custo_inst)

print(f"O valor total do sistema ficou em: R$ {total:.2f}")
