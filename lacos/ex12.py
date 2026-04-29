saldo = 1000.0
historico = []

while True:
    print("\n=== CAIXA ELETRONICO ===")
    print("a) Depositar")
    print("b) Sacar")
    print("c) Ver saldo")
    print("d) Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "a":
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor <= 0:
            print("Erro: o depósito deve ser um valor positivo.")
        else:
            saldo += valor
            print(f"Depósito realizado. Novo saldo: R$ {saldo:.2f}")
            historico.append(f"Depósito de R$ {valor:.2f}")

    elif opcao == "b":
        valor = int(input("Digite o valor do saque (inteiro): R$ "))

        if valor <= 0:
            print("Erro: o saque deve ser um valor positivo.")
        elif valor % 2 != 0:
            print("Erro: o saque deve ser múltiplo de 2.")
        elif valor > saldo:
            print("Erro: saldo insuficiente.")
        else:
            restante = valor

            notas_100 = restante // 100
            restante = restante % 100

            notas_50 = restante // 50
            restante = restante % 50

            notas_20 = restante // 20
            restante = restante % 20

            notas_10 = restante // 10
            restante = restante % 10

            notas_5 = restante // 5
            restante = restante % 5

            notas_2 = restante // 2
            restante = restante % 2

            if restante != 0:
                print("Erro: não foi possível calcular notas para esse saque.")
            else:
                saldo -= valor
                print(f"Saque realizado. Novo saldo: R$ {saldo:.2f}")
                print("Notas entregues:")
                print(f"100: {notas_100}")
                print(f"50: {notas_50}")
                print(f"20: {notas_20}")
                print(f"10: {notas_10}")
                print(f"5: {notas_5}")
                print(f"2: {notas_2}")
                historico.append(f"Saque de R$ {valor:.2f}")

    elif opcao == "c":
        print(f"Saldo atual: R$ {saldo:.2f}")
        historico.append("Consulta de saldo")

    elif opcao == "d":
        print("\n=== RESUMO FINAL ===")
        print(f"Saldo final: R$ {saldo:.2f}")
        print(f"Total de operações registradas: {len(historico)}")

        if len(historico) == 0:
            print("Nenhuma operação registrada.")
        else:
            print("Últimas operações:")
            inicio = 0
            if len(historico) > 10:
                inicio = len(historico) - 10

            for i in range(inicio, len(historico)):
                print(f"- {historico[i]}")

        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida. Tente novamente.")
