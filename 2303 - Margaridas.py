linhas, colunas, linhas_lote, colunas_lote = map(int, input().split())
margaridas = []
for lin in range(linhas):
    margaridas.append(list(map(int, input().split())))
maior = -1
for primeira_lin in range(0, linhas, linhas_lote):
    for primeira_col in range(0, colunas, colunas_lote):
        soma = 0
        for lin in range(primeira_lin, primeira_lin + linhas_lote):
            for col in range(primeira_col, primeira_col + colunas_lote):
                soma += margaridas[lin][col]
        if maior < soma:
            maior = soma
print(maior)
