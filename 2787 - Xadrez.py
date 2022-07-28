linhas = int(input())
colunas = int(input())
tabuleiro = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        if (i+j) % 2 == 0:
            linha.append(1)
        else:
            linha.append(0)
    tabuleiro.append(linha)

for i in range(linhas-1, linhas):
    for j in range(colunas-1, colunas):
        print(tabuleiro[i][j])
