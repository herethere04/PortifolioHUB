
d = int(input('Qual distancia da viajem ? km: '))
v1 = d * 0.50
v2 = d * 0.45
if d <= 200 :
    print(f'Sua viajem é de até 200km portanto custará R${v1}')
elif d > 200 :
    print(f'Sua viajem é de mais de 200km portanto custará R${v2}')