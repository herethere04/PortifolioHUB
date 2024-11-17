from datetime import date
ano = int(input('Em q ano vc nasceu ?'))
atual = date.today().year
idade = (ano - atual) *-1
if idade < 18 :
    print('Voçê nasceu em {} e têm {} anos em {}'.format(ano, idade, atual))
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o seu alistamento e vc devará se alistar em {}'.format(saldo, ano))
elif idade == 18 :
    print('Já é hora de se alistar.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Voçê já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}')