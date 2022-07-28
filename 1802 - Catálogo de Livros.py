port = list(map(int, input().split()))
mat = list(map(int, input().split()))
fis = list(map(int, input().split()))
quim = list(map(int, input().split()))
bio = list(map(int, input().split()))
total = int(input())

port.pop(0)
mat.pop(0)
fis.pop(0)
quim.pop(0)
bio.pop(0)

port.sort()
mat.sort()
fis.sort()
quim.sort()
bio.sort()

precos = []

for i in range(len(port)):
    for j in range(len(mat)):
        for k in range(len(fis)):
            for l in range(len(quim)):
                for m in range(len(bio)):
                    x = port[i] + mat[j] + fis[k] + quim[l] + bio[m]
                    precos.append(x)

precos.sort(reverse=True)
result = 0
for i in range(total):
    result += precos[i]

print(result)
