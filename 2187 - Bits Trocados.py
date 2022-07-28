teste = 0
while 1:
    bits = int(input())
    if bits == 0:
        break
    else:
        teste += 1
        print('Teste {}'.format(teste))
        num_50 = bits // 50
        bits = bits - (50*num_50)
        num_10 = bits // 10
        bits = bits - (10*num_10)
        num_5 = bits // 5
        bits = bits - (5*num_5)
        num_1 = bits // 1
        bits = bits - (1*num_1)
        print('{} {} {} {}'.format(num_50, num_10, num_5, num_1))
        print()
