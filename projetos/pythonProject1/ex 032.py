ano = int(input('Qual o ano ?'))
if ano % 4 and ano % 100 != 0 or ano% 400 == 0 :
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} n é um ano bissexto')