v = int(input('Qual a velocidade do carro em km/h ?'))
multa = (v - 80) * 7
if v > 80:
    print('Vc ultrapassou o limite de velocidade sua multa será de R${}'.format(multa))
else:
    print('Parabens vc está no limite de velocidade continue assim.')