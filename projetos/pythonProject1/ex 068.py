import random
from time import sleep
print('=-' * 30)
print('VAMOS JOGAR IMPAR OU PAR')
print('=-' * 30)
sleep(0.5)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = random.choice(lista)
cont = 0
while True:
    jogador = int(input('Escolha um numero de 1 á 10 :'))
    escolha = str(input('Par ou Ímpar: [P/I] :')).strip().lower()[0]
    print('=-' * 30)
    resultado = (computador + jogador) % 2
    print(f'Você jogou {jogador} e o computador jogou {computador}. Deu {jogador + computador}')
    if resultado == 1 and escolha == 'i':
        print('VC VENCEU, vamos jogar novamente')
        print('=-' * 30)
        cont += 1
    if resultado == 0 and escolha == 'i':
        print('VC PERDEU !!!')
        print('=-' * 30)
        break
    if resultado == 1 and escolha == 'p':
        print('VC PERDEU !!!')
        print('=-' * 30)
        break
    if resultado == 0 and escolha == 'p':
        print('VC VENCEU, vamos jogar novamente')
        print('=-' * 30)
        cont += 1
if cont != 0:
    print(f'Vc ganhou {cont} vezes consecutivas ')
print('GAME OVER')
