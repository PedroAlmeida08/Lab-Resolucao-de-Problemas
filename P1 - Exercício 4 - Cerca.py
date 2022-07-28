ct = 0
num_cercas, altura_final = input().split()
num_cercas = int(num_cercas)
altura_final = int(altura_final)
altura_cercas = input().split()
altura = [0] * num_cercas
for i in range(num_cercas):
    altura[i] = int(altura_cercas[i])
for i in range(num_cercas-1):
    if altura[i] > altura[i+1]:
        while altura[i] != altura[i+1]:
            altura[i+1] += 1
            altura[i+2] += 1
            ct += 1
    elif altura[0] < altura[1]:
        while altura[i] != altura[i]:
            altura[i+1] -= 1
            altura[i+2] -= 1
            ct += 1
    while altura[i] != altura_final and altura[i+1] != altura_final:
        if altura[i] > altura_final and altura[i+1] > altura_final:
            altura[i] -= 1
            altura[i+1] -= 1
            ct += 1
        elif altura[i] < altura_final and altura[i+1] < altura_final:
            altura[i] += 1
            altura[i+1] += 1
            ct += 1
print(ct)
