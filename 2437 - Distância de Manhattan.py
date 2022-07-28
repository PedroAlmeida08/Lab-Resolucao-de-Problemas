x_m, y_m, x_r, y_r = map(int, input().split())
crz = 0
while x_m != x_r:
    crz += 1
    if x_m > x_r:
        x_r += 1
    else:
        x_m += 1
while y_m != y_r:
    crz += 1
    if y_m > y_r:
        y_r += 1
    else:
        y_m += 1
print(crz)
