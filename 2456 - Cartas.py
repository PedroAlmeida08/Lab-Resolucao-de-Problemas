C = 0
D = 0
cartas = input().split()
cartas[0] = int(cartas[0])
for i in range(1,5):
    cartas[i] = int(cartas[i])
    if cartas[i-1] < cartas[i]:
        C += 1
    else:
        D += 1
if C == 4:
    print('C')
elif D == 4:
    print('D')
else:
    print('N')
