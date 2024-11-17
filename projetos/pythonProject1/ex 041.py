idade = int(input('Idade do atleta :'))
if idade <= 9 :
    print('Voçê é um atleta MIRIM')
elif idade <= 14 :
    print('Voçê é um atleta INFANTIL')
elif idade <= 19 :
    print('Voçê é um atleta JUNIOR')
elif idade <= 20 :
    print('Voçê é um atleta SÊNIOR')
else:
    print('Voçê é um atleta MASTER')