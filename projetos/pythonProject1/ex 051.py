print('10 TERMOS DE UMA P.A')
p = int(input('Primeiro termo :'))
r = int(input('Razão : '))
d = p + 10 * r
for c in range(p, d, r):
    print(c)
