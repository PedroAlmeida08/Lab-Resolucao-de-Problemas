linhas, colunas, linha_caju, coluna_caju = map(int, input().split())

cajus = []
for i in range(linhas):
    cajus.append(list(map(int, input().split())))

acumulado = [[0] * (colunas + 1) for i in range(linhas + 1)]
for i in range(1, linhas + 1):
    for j in range(1, colunas + 1):
        acumulado[i][j] = acumulado[i - 1][j] + acumulado[i][j - 1] - acumulado[i - 1][j - 1] + cajus[i - 1][j - 1]

max_soma = -1
for i in range(linha_caju, linhas + 1):
    for j in range(coluna_caju, colunas + 1):
        soma = acumulado[i][j] - acumulado[i - linha_caju][j] - acumulado[i][j - coluna_caju] + acumulado[i - linha_caju][j - coluna_caju]
        if max_soma < soma:
            max_soma = soma
print(max_soma)
