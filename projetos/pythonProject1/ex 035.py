a = float(input('Reta 1 :'))
b = float(input('Reta 2 :'))
c = float(input('Reta 3 :'))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b :
    print('As retas podem formar um triangulo')
else :
    print('N tem como formar um triangulo')