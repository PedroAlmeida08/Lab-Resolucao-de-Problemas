prec_alc, prec_gas, rend_alc, rend_gas = map(float, input().split())
if (prec_alc/rend_alc) < (prec_gas/rend_gas):
    print('A')
else:
    print('G')
