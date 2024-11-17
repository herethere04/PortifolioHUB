import math
co = float(input('Cateto oposto : '))
ca = float(input('Cateto adjascente : '))
c1 = co ** 2
c2 = ca ** 2
s = c1 + c2
h = math.sqrt(s)
print('A hipotenusa é igual a {:.2f} ' .format(h))
#pra fazer a raiz quadrada de qqlr coisa é só fazer (1/2)
# e pra fazer com o math é só math.hypot
