peso = float(input('Qual seu peso em KG:'))
altura = float(input('Qual a sua altura :'))
imc = peso / (altura * altura)
if imc <= 18.5:
    print('Seu imc é de {:.1f} portanto vc esta abaixo do peso'.format(imc))
elif imc < 25:
    print('Seu imc é de {:.1f} portanto vc esta com o peso ideal'.format(imc))
elif imc < 30:
    print('Seu imc é de {:.1f} portanto vc esta com sobrepeso'.format(imc))
elif imc < 40:
    print('Seu imc é de {:.1f} portanto vc esta obeso'.format(imc))
else:
    print('Seu imc é de {:.1f} portanto vc esta com obesidade morbida'.format(imc))