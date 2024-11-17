frase = str(input('Digite uma frase para saber se ela é um palindromo ou n :')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('{}, {}'.format(junto, inverso))
if junto == inverso:
    print('É um palindromo')
else:
    print('N é um palindromo')