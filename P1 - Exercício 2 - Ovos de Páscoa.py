from math import sqrt, pow
largura, altura, profundidade, raio = input().split()
largura = int(largura)
altura = int(altura)
profundidade = int(profundidade)
raio = int(raio)
diametro_min = sqrt((pow(largura, 2) + pow(altura, 2) + pow(profundidade, 2)))
if diametro_min <= (raio * 2):
    print('S')
else:
    print('N')
