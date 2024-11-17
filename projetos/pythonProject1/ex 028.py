import random
n = int(input('Tente advinhar um numero de 1 a 5 : '))
lista = [ 1, 2, 3, 4, 5]
numero = random.choice(lista)
if n == numero:
    print('Parabens vc acertou era {}'.format(numero))
else:
    print('Vc errou era {} e vc chutou {}, boa sorte na proxima.'.format(numero,n))