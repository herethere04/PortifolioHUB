soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'digite o valor {c} inteiro :'))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Voçê informou {} números pares e a soma foi {}'.format(cont, soma))