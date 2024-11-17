print('-=' * 20)
print('MERCADINHO DO SEU ZÉ')
print('-=' * 20)
cont = menor = total = totmil = 0
barato = ''
while True:
    produto = str(input('Nome do produto :')).strip()
    preço = int(input('Preço do produto : R$'))
    cont += 1
    total += preço
    if preço >= 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar [S/N] :')).strip().upper()[0]
    if escolha == 'N':
        break
print('O total da compra foi : R$ {:.2f}'.format(total))
print(f'O total de produtos acima de mil reais foi : {totmil}')
print(f'O produtos mais barato e seu preço foram : {barato}, R${menor}')