senha_correta = "salvee12"
tentativas = 0
acesso_liberado = False

while tentativas < 3 and acesso_liberado == False:
    senha_digitada = input("Digite a senha: ")
    tentativas += 1

    if senha_digitada == senha_correta:
        acesso_liberado = True
        print("Login realizado com sucesso.")
    else:
        print("Senha incorreta.")

if acesso_liberado == False:
    print("Acesso bloqueado após 3 tentativas.")

print(f"Tentativas usadas: {tentativas}")
