teste = 0
participantes, rodadas = map(int, input().split())
while participantes != 0 and rodadas != 0:
    teste += 1
    print('Teste {}'.format(teste))
    x = list(map(int, input().split()))
    for i in range(rodadas):
        rodada = list(map(int, input().split()))
        a = rodada[0]
        b = rodada[1]
        aux = []
        for j in range(a):
            if rodada[j + 2] == b:
                aux.append(x[j])
        x = aux
    print(x[0])
    print()
    participantes, rodadas = map(int, input().split())
