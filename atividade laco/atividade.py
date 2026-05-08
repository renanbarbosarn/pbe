usuario = "admin"
senha = "1234"
tentativas_acesso = 3
produtos = dict()
vendas = {
    "historico_codigo": list(),
    "historico_produto": list(),
    "historico_qtd": list(),
    "historico_valor": list()
}
opcao_escolhida = None

while tentativas_acesso > 0 and opcao_escolhida != "6":
    print(f"{'LOGIN':^24}")
    print(f"TENTATIVAS RESTANTES: {tentativas_acesso}")
    login = {
        "usuario": input("Usuário: "),
        "senha": input("Senha: ")
    }
    

    if login["usuario"] == usuario and login["senha"] == senha:
        while True:
            print()
            print(f"{'Menu de Opções':^20}")
            print("1: Cadastrar produto")
            print("2: Listar produtos")
            print("3: Atualizar estoque")
            print("4: Realizar venda")
            print("5: Relatórios")
            print("6: Sair")

            opcao_escolhida = input("\nOPÇÃO --> ")
            print()

            match opcao_escolhida:
                case "1":
                    print(F"{'CADASTRAR PRODUTO':^59}\n" + "-" * 59)
                    codigo = int(input("Código: "))
                    
                    if codigo not in produtos:
                        produtos[codigo] = {                
                            "nome": input("Nome: "),
                            "preco": float(input("Preço: ")),
                            "quantidade": int(input("Quantidade: "))
                        }

                        print(len(produtos))
                    else:
                        print("Um produto com este código já está cadastrado!\n")

                case "2":
                    print(F"{'PRODUTOS CADASTRADOS':^59}\n" + "-" * 59)

                    if not produtos.items():
                        print("Nenhum produto cadastrado")
                    else:
                        print(f"{'Código':<10} | {'Nome':<20} | {'Preço':<12} | {'Estoque':<10}\n" + "-" * 59)
                        for produto in produtos:
                            print(f"{f'{produto}':<10} | {f'{produtos[produto]["nome"]}':<20} | {f'R$ {produtos[produto]["preco"]:.2f}':<12} | {f'{produtos[produto]["quantidade"]}':<10}")

                case "3":
                    print(F"{'ATUALIZAR ESTOQUE':^59}\n" + "-" * 59)
                    atualizar_produto = int(input("Informe o código do produto que quer alterar: "))

                    if not atualizar_produto in produtos:
                        print(f"O produto com o código '{atualizar_produto}' não existe!")
                    
                    else:
                        print(f"\n{'Código':<10} | {'Nome':<20} | {'Preço':<12} | {'Estoque':<10}\n" + "-" * 59)
                        print(f"{f'{atualizar_produto}':<10} | {f'{produtos[atualizar_produto]["nome"]}':<20} | R$ {f'{produtos[atualizar_produto]["preco"]}':<12} | {f'{produtos[atualizar_produto]["quantidade"]:}':<10}")
                        
                        print("\nMENU")
                        print("1: Adicionar estoque")
                        print("2: Remover estoque")

                        opcao_escolhida = input("\nOPÇÃO --> ")
                        print()

                        match opcao_escolhida:
                            case "1":
                                produtos[atualizar_produto]["quantidade"] += int(input("\nDigite o quanto quer adicionar: "))
                                print(f"Adicionado! Agora tem {produtos[atualizar_produto]["quantidade"]} unidades no estoque.")

                            case "2":
                                remover = int(input("\nDigite o quanto quer remover: "))

                                if produtos[atualizar_produto]["quantidade"] - remover < 0:
                                    print(f"Não é possível remover {remover} unidade(s), pois negativará o número do estoque!")
                                else: 
                                    produtos[atualizar_produto]["quantidade"] -= remover

                                    print(f"Removido! Agora tem {produtos[atualizar_produto]["quantidade"]} unidades no estoque.")

                            case _:
                                print("\nOPÇÃO INVÁLIDA!\n")

                case "4": 
                    print(F"{'REALIZAR VENDA':^59}\n" + "-" * 59)
                    atualizar_produto = int(input("Informe o código do produto que irá vender: "))

                    if not atualizar_produto in produtos:
                        print(f"O produto com o código '{atualizar_produto}' não existe!")
                    else:
                        print(f"\n{'Código':<10} | {'Nome':<20} | {'Preço':<12} | {'Estoque':<10}\n" + "-" * 59)
                        print(f"{f'{atualizar_produto}':<10} | {f'{produtos[atualizar_produto]["nome"]}':<20} | R$ {f'{produtos[atualizar_produto]["preco"]}':<12} | {f'{produtos[atualizar_produto]["quantidade"]:}':<10}")

                        qtd_desejada = int(input("\nDigite a quantidade desejada: "))

                        if produtos[atualizar_produto]["quantidade"] - qtd_desejada < 0:
                            print("Infelizmente não temos essa quantidade no estoque!")
                        else:
                            produtos[atualizar_produto]["quantidade"] -= qtd_desejada

                            valor_total = produtos[atualizar_produto]["preco"] *qtd_desejada

                            print(f"Estoque atualizado para {produtos[atualizar_produto]["quantidade"]} unidadese e venda registrada.")

                            vendas["historico_codigo"].append(atualizar_produto)
                            vendas["historico_produto"].append(produtos[atualizar_produto]["nome"])
                            vendas["historico_qtd"].append(qtd_desejada)
                            vendas["historico_valor"].append(valor_total)
                        
                            print(f"Venda no valor de R$ {valor_total:.2f} registrada com sucesso!")
                case "5":
                    if vendas["historico_produto"] and vendas["historico_qtd"]:
                        vendas_por_produto = {}
                        for prod, qtd in zip(vendas["historico_produto"], vendas["historico_qtd"]):
                            vendas_por_produto[prod] = vendas_por_produto.get(prod, 0) + qtd
                        produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)
                        nome_produto_mais_vendido = produto_mais_vendido
                    else:
                        nome_produto_mais_vendido = "-"
                    
                    if produtos:
                        produto_maior_estoque = max(
                            produtos, key=lambda produto_id: produtos[produto_id]["quantidade"]
                        )
                        nome_produto_maior_estoque = produtos[produto_maior_estoque]["nome"]
                    else:
                        nome_produto_maior_estoque = "-"

                    print(f"\n{'Total vendido':<14} | {'Produto mais vendido':<21} | {'Maior estoque'}\n" + "-" * 56)
                    print(f"{sum(vendas['historico_qtd']):<14} | {nome_produto_mais_vendido:<21} | {nome_produto_maior_estoque}")
         

                    print(F"{"\nVENDAS REGISTRADAS":^59}\n" + "-" * 63)
                    print(f"{'Código':<10} | {'Nome':<20} | {'Preço':<12} | {'Quantidade':<10}\n" + "-" * 63)
                    for cod, nam, prec, qtd in zip(vendas["historico_codigo"], vendas["historico_produto"], vendas["historico_valor"], vendas["historico_qtd"]):
                        print(f"{cod:<10} | {nam:<20} | {prec:<12} | {qtd:<10}")
                    

                case "6":
                    total_produtos_cadastrados = len(produtos)
                    total_vendas_realizadas = len(vendas["historico_qtd"])
                    valor_total_vendido = sum(vendas["historico_valor"])

                    print(f"\n{'RESUMO DE SAÍDA':^63}\n" + "-" * 80)
                    print(f"{'Total de produtos cadastrados':<30} | {'Total de vendas realizadas':<27} | {'Valor total vendido':<20}\n" + "-" * 80)
                    print(f"{total_produtos_cadastrados:<30} | {total_vendas_realizadas:<27} | R$ {valor_total_vendido:.2f}")
               
                    break
                case _:
                    print("\nOPÇÃO INVÁLIDA!\n")

    else:
        tentativas_acesso -= 1
        print()
    
