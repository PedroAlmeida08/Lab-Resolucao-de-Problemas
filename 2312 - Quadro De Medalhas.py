from _functools import cmp_to_key


def cmp(pais_1, pais_2):

    if pais_1[1] > pais_2[1] or (pais_1[1] == pais_2[1] and pais_1[2] > pais_2[2]) or (
            pais_1[1] == pais_2[1] and pais_1[2] == pais_2[2] and pais_1[3] > pais_2[3]) or (
            pais_1[1] == pais_2[1] and pais_1[2] == pais_2[2] and pais_1[3] == pais_2[3] and pais_1[0] < pais_2[0]):
        return -1
    elif pais_1[1] < pais_2[1] or (pais_1[1] == pais_2[1] and pais_1[2] < pais_2[2]) or (
            pais_1[1] == pais_2[1] and pais_1[2] == pais_2[2] and pais_1[3] < pais_2[3]) or (
            pais_1[1] == pais_2[1] and pais_1[2] == pais_2[2] and pais_1[3] == pais_2[3] and pais_1[0] > pais_2[0]):
        return +1
    else:
        return 0


n = int(input())
lista = []
for i in range(n):
    lista.append(input().split())

for i in range(n):
    lista[i][1] = int(lista[i][1])
    lista[i][2] = int(lista[i][2])
    lista[i][3] = int(lista[i][3])

lista.sort(key=cmp_to_key(cmp))

for i in range(n):
    print(lista[i][0], lista[i][1], lista[i][2], lista[i][3])
