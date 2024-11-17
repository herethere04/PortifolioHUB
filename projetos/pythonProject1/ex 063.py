n = int(input('Quantos termos da sequência de Fibonacci vc quer mostrar:'))
primeiro = 0
segundo = 1
cont = 3
print('{} , {} ,'.format(primeiro, segundo), end='')
while cont <= n:
    terceiro = primeiro + segundo
    print(f' {terceiro} ,', end='')
    primeiro = segundo
    segundo = terceiro
    cont += 1
print(' FIM')
