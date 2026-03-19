tamanho_mb = float(input("Qual o tamanho do arquivo em MB? "))
qtd = int(input("Quantos arquivos você baixou? "))

total_gb = (tamanho_mb * qtd) / 1024

print(f"O tamanho total dos arquivos é de {total_gb:.2f} GB")
