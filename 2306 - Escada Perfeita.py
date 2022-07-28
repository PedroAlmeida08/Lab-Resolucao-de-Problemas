from math import pow
n = int(input())
linha = list(map(int, input().split()))
soma = sum(linha)
soma -= (pow(n, 2) + n) // 2
if soma >= 0 and (soma % n) == 0:
    mov = 0
    altura = (soma // n) + 1
    for i in range(n):
        if linha[i] > altura:
            mov += linha[i] - altura
        altura += 1
    print(int(mov))
else:
    print(-1)
