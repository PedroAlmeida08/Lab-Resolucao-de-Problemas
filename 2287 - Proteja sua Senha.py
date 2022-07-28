teste = 0
n = int(input())
while n != 0:
    teste += 1
    print('Teste {}'.format(teste))
    ct = [0] * 10 * 6

    for i in range(n):
        cod = input().split()
        num = list(map(int, cod[0:10]))
        let = cod[10:16]

        for j in range(6):
            letra = let[j]
            n1 = n2 = -1
            if letra == 'A':
                n1, n2 = num[0], num[1]
            elif letra == 'B':
                n1, n2 = num[2], num[3]
            elif letra == 'C':
                n1, n2 = num[4], num[5]
            elif letra == 'D':
                n1, n2 = num[6], num[7]
            elif letra == 'E':
                n1, n2 = num[8], num[9]

            ct[10 * j + n1] += 1
            ct[10 * j + n2] += 1

    for j in range(6):
        freq = ct[10 * j : 10 * (j + 1)]
        m_freq = -1
        senha = None
        for k in range(10):
            if m_freq < freq[k]:
                m_freq = freq[k]
                senha = k
        print(senha, end=' ')
    print('\n')

    n = int(input())
