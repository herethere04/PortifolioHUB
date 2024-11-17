cont = 0
total = 0
maior = 0
menor = 0
escolha = 's'
while escolha != 'n':
    n = int(input('Digite um numero :'))
    escolha = str(input('Quer continuar ? [S/N] :')).strip().lower()[0]
    total += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = total / cont
print('Vc digitou {} numeros e a media foi {:.2f}'.format(cont, media))
print('O maior valor é {} e o menor é {}'.format(maior, menor))
