n = int(input())
escadinhas = 1
lista = list(map(int, input().split()))
for i in range(2, n):
    if (lista[i] - lista[i-1]) != (lista[i-1] - lista[i-2]):
        escadinhas += 1
print(escadinhas)
