from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input('Qual seu ano de nascimento pessoa n° {} :'.format(c)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Têm {} pessoas maior de idade e {} menores de idade.'.format(totmaior, totmenor))
