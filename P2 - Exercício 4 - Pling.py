n = int(input())
cartas = input().split()

for i in range(n):
    cartas[i] = int(cartas[i])

result = 0
lista_result = []
if len(cartas) == 1:
    print(1)
elif len(cartas) == 2:
    if cartas[0] == cartas[1]:
        print(2)
    else:
        print(1)
else:
    a = cartas[0]
    b = cartas[1]
    for i in range(2, len(cartas)):
        if a == b:
            result += 1
        else:
            lista_result.append(result)
            result = 0
        a = b
        b = cartas[i]
    print(max(lista_result)+1)
