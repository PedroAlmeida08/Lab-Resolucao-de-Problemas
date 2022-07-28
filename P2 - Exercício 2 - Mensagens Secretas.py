lista = input()
a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]
e = lista[4]
f = lista[5]
g = lista[6]
h = lista[7]
i = lista[8]
j = lista[9]
k = lista[10]
l = lista[11]
m = lista[12]
n = lista[13]
o = lista[14]
p = lista[15]
q = lista[16]
r = lista[17]
s = lista[18]
t = lista[19]
u = lista[20]
v = lista[21]
w = lista[22]
x = lista[23]
y = lista[24]
z = lista[25]

cod = input()

resp = []

for ct in range(len(cod)):
    if cod[ct] == 'a':
        resp.append(a)
    elif cod[ct] == 'b':
        resp.append(b)
    elif cod[ct] == 'c':
        resp.append(c)
    elif cod[ct] == 'd':
        resp.append(d)
    elif cod[ct] == 'e':
        resp.append(e)
    elif cod[ct] == 'f':
        resp.append(f)
    elif cod[ct] == 'g':
        resp.append(g)
    elif cod[ct] == 'h':
        resp.append(h)
    elif cod[ct] == 'i':
        resp.append(i)
    elif cod[ct] == 'j':
        resp.append(j)
    elif cod[ct] == 'k':
        resp.append(k)
    elif cod[ct] == 'l':
        resp.append(l)
    elif cod[ct] == 'm':
        resp.append(m)
    elif cod[ct] == 'n':
        resp.append(n)
    elif cod[ct] == 'o':
        resp.append(o)
    elif cod[ct] == 'p':
        resp.append(p)
    elif cod[ct] == 'q':
        resp.append(q)
    elif cod[ct] == 'r':
        resp.append(r)
    elif cod[ct] == 's':
        resp.append(s)
    elif cod[ct] == 't':
        resp.append(t)
    elif cod[ct] == 'u':
        resp.append(u)
    elif cod[ct] == 'v':
        resp.append(v)
    elif cod[ct] == 'w':
        resp.append(w)
    elif cod[ct] == 'x':
        resp.append(x)
    elif cod[ct] == 'y':
        resp.append(y)
    elif cod[ct] == 'z':
        resp.append(z)

for ct_aux in range(len(cod)):
    print(resp[ct_aux], end='')
