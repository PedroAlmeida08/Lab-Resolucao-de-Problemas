num_bandejas = int(input())
quebra = 0
for i in range(num_bandejas):
    latas, copos = map(int, input().split())
    if latas > copos:
        quebra += copos
print(quebra)
