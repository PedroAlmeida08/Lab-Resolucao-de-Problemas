n = int(input())
for i in range(n):
    texto = input().strip().split()
    aux1 = []
    aux2 = []
    for j in texto:
        if j != "":
            aux1.append(j)
    for k in aux1:
        aux2.append(k[0])
    print(''.join(aux2))
