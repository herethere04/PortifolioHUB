'''lista = ('banana', 1.25, 'maçã fuji', 5.99, 'melância', 8.99, 'morango', 5.99,
         'mamão', 3.99, 'frango', 15.50, 'acém', 22.25, 'carne moida', 21.55,
         'costela', 27.99)
print('_'*40)
print(str('Listagem de preços'.upper()))
print('_'*40)
print(lista[0], '.'*10,'R$',lista[1])
print(lista[2], '.'*10,'R$',lista[3])
print(lista[4], '.'*10,'R$',lista[5])
print(lista[6], '.'*10,'R$',lista[7])
print(lista[8], '.'*10,'R$',lista[9])
print(lista[10], '.'*10,'R$',lista[11])
print(lista[12], '.'*10,'R$',lista[13])
print(lista[14], '.'*10,'R$',lista[15])
print(lista[16], '.'*10,'R$',lista[17])
print('_'*40)'''

lista = ('banana', 1.25, 'maçã fuji', 5.99, 'melância', 8.99, 'morango', 5.99,
         'mamão', 3.99, 'frango', 15.50, 'acém', 22.25, 'carne moida', 21.55,
         'costela', 27.99)
print('-'*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)