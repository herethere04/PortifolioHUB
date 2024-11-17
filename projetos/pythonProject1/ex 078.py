valores = []
menor = maior = 0
for c in range(0,5):
    valores.append(int(input('Digite um valor :')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 30)
print(f'Voçê digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições : ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print('')
print(f'O menor valor foi {menor} nas posições : ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print('')