import sys
min_esforco = sys.maxsize
t_min = None
n = int(input())
for i in range(1, n+1):
    linha = list(map(int, input().split()))
    esf_ida = 0
    esf_volta = 0
    a = linha[1]
    for j in range(2, linha[0]+1):
        b = linha[j]
        if a <= b:
            esf_ida += (b - a)
        else:
            esf_volta += (a - b)
        a = b
    esforco = min(esf_ida, esf_volta)
    if min_esforco > esforco:
        min_esforco = esforco
        t_min = i
print(t_min)
