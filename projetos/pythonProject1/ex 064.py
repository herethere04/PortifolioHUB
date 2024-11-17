n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar] :'))
    soma += n
    cont += 1
print('Foram feitos {} tentativas e a soma de todos é {}.'.format(cont - 1, soma - 999))
