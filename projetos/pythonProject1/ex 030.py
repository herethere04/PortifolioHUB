import math
n = int(input('Digite um numero :'))
resultado = n % 2
if resultado == 0 :
    print('{} é um numero par'.format(n))
else:
    print('{} é um numero impar'.format(n))