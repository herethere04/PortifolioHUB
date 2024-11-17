from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções :
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada : '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('-=' * 13)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 13)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Jogador perde')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('Jogador perdeu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Jogador perde')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')












#import random
#print('''[ 1 ] Pedra
#[ 2 ] Papel
#[ 3 ] Tesoura''')
#a = input(':')
#lista = ['Pedra', 'Papel', 'Tesoura' ]
#r = (random.choice(lista))
#if a == 1 and r == lista[0]:
#    print('Deu pedra x pedra portanto deu impate')
#print(r)