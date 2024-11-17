print('=' * 40)
print('{:-^40}'.format('BANCO DA CASA DO KRL'))
print('=' * 40)
tot50 = tot20 = tot10 = tot1 = resto = 0
valor = int(input('Que valor vc quer sacar ? R$'))
while True:
    if valor >= 50:
        tot50 = valor // 50
        resto = valor - (tot50 * 50)
    if resto >= 20:
        tot20 = resto // 20
        resto = resto - (tot20 * 20)
    if resto >= 10:
        tot10 = resto // 10
        resto = resto - (tot10 * 10)
    if resto <= 9:
        tot1 = resto // 1
        resto = resto - (tot1 * 1)
    if resto == 0:
        break
if tot50 != 0:
    print(f'Total de {tot50} cédulas de R$50')
if tot20 != 0:
    print(f'Total de {tot20} cédulas de R$20')
if tot10 != 0:
    print(f'Total de {tot10} cédulas de R$10')
if tot1 != 0:
    print(f'Total de {tot1} cédulas de R$1')
