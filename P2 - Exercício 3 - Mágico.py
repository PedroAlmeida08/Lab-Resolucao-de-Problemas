y, z, v, w = map(int, input().split())
x = 1
while 1:
    if (x % y) == 0:
        if (x % z) != 0:
            if (v % x) == 0:
                if (w % x) != 0:
                    print(x)
                    break
    if x < 1000000 - 1:
        x += 1
    else:
        print(-1)
        break
