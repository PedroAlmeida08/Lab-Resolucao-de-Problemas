lim = int(input())
num_1, op, num_2 = input().split()
num_1 = int(num_1)
num_2 = int(num_2)
if op == '+':
    calc = num_1 + num_2
elif op == '-':
    calc = num_1 - num_2
elif op == '*':
    calc = num_1 * num_2
else:
    calc = num_1 / num_2
if calc > lim:
    print('OVERFLOW')
else:
    print('OK')
