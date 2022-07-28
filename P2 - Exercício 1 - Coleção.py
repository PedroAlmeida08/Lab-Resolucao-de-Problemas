vol_lan, vol_exi, vol_comp = map(int, input().split())
exi = list(map(int, input().split()))
comp = list(map(int, input().split()))

result = vol_exi

for i in range(vol_exi):
    for j in range(vol_comp):
        if exi[i] == comp[j]:
            comp.pop(j)
            vol_comp -= 1
            result -= 1
            break

print(result)
