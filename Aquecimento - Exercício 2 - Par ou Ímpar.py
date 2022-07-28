teste = 0
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        teste += 1
        print(f'Teste {teste}')
        nome_par = input()
        nome_impar = input()
        for i in range(n):
            a, b = input().split()
            a = int(a)
            b = int(b)
            if (a + b) % 2 == 0:
                print(nome_par)
            else:
                print(nome_impar)
        print()
