prim = int(input())
seg = int(input())
ter = int(input())
maior = max(prim, seg, ter)
tmp = [0] * 3
tmp[0] = (seg * 2) + (ter * 4)
tmp[1] = (prim * 2) + (ter * 2)
tmp[2] = (prim * 4) + (seg * 2)
if tmp[0] <= tmp[1] and tmp[0] <= tmp[2]:
    print(tmp[0])
elif tmp[1] <= tmp[0] and tmp[1] <= tmp[2]:
    print(tmp[1])
else:
    print(tmp[2])
