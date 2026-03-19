quantidade_arquivos = int(input("Quantidade de arquivos: "))
tamanho_arquivo = float(input("Tamanho médio de cada arquivo (em megabytes): "))

mb_em_gb = quantidade_arquivos * tamanho_arquivo / 1024

print(f"O espaço ocupado é de {mb_em_gb:.1f} GB.")
