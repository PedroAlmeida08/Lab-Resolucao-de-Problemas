mapa = [False] * 501 * 501
result = 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    coord = x * 501 +y
    if mapa[coord] == True:
        result = 1
        break
    else:
        mapa[coord] = True
print(result)
