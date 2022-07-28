carta_1, carta_2 = map(int, input().split())
melhor = 0
if carta_1 == carta_2:
    melhor = carta_1
else:
    if carta_1 > carta_2:
        melhor = carta_1
    else:
        melhor = carta_2
print(melhor)
