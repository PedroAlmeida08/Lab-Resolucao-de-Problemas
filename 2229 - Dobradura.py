from math import pow
teste = 0
ct = 0
n = int(input())
while n != -1:
    teste += 1
    print('Teste {}'.format(teste))
    if n == 0:
        quad = 4
    elif n == 1:
        quad = 9
    else:
        quad = pow(pow(2, n)+1, 2)
    print(int(quad))
    print()
    n = int(input())
