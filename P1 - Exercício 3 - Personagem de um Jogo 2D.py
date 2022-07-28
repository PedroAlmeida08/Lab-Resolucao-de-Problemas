num_test = int(input())
for i in range(num_test):
    num_passos = int(input())
    pos = 0
    ct = [''] * (num_passos + 1)
    for j in range(1, num_passos + 1):
        passo = input()
        if passo == 'ESQ':
            pos -= 1
            ct[j] = 'SUB'
        elif passo == 'DIR':
            pos += 1
            ct[j] = 'SOMA'
        elif 'EXEC' in passo:
            passo.split()
            a = passo[5]
            a = int(a)
            if ct[a] == 'SOMA':
                pos += 1
                ct[j] = 'SOMA'
            elif ct[a] == 'SUB':
                pos -= 1
                ct[j] = 'SUB'
    print(pos)
