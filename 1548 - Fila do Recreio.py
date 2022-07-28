n = int(input())
for i in range(n):
    alunos = int(input())
    notas = list(map(int, input().split()))
    notas_org = sorted(notas, reverse=True)
    for j in range(alunos):
        if notas[j] != notas_org[j]:
            alunos -= 1
    print(alunos)
