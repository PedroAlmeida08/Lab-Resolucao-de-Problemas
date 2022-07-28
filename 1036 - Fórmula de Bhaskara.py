import math

incognita = input().split()
a = float(incognita[0])
b = float(incognita[1])
c = float(incognita[2])

delta = (b**2) - (4*a*c)

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + math.sqrt(delta))/(2*a)
    r2 = (-b - math.sqrt(delta))/(2*a)
    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)
