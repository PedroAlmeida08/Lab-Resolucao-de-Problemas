teste = 0
n, m = map(int, input().split())
while n != 0 or m != 0:
    teste += 1
    print("Teste {}".format(teste))
    soma_acumulada = [None] * n
    soma_acumulada[0] = int(input())
    for i in range(1, n):
        soma_acumulada[i] = soma_acumulada[i - 1] + int(input())
    min_soma = max_soma = soma_acumulada[m - 1]
    for j in range(m, n):
        soma = soma_acumulada[j] - soma_acumulada[j - m]
        min_soma = min(soma, min_soma)
        max_soma = max(soma, max_soma)
    print("{} {}".format(int(min_soma / m), (int(max_soma / m))))
    print()
    n, m = map(int, input().split())
