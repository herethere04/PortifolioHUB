a = float(input('Reta 1 :'))
b = float(input('Reta 2 :'))
c = float(input('Reta 3 :'))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b :
    print('As retas podem formar um triangulo')
    if a == b == c:
        print('É um triangulo equilatero')
    elif a == b or b == c or c == a :
        print('É um triangulo isosceles')
    else:
        print('É um triangulo escaleno')
else :
    print('N tem como formar um triangulo')
# pra fazer a diferença é só usar (exclamaçao =)