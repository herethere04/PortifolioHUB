from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
sleep(1.8)
print('Será q vc consegue adivinhar qual foi ? ')
sleep(1)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite : '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente.')
        elif jogador > computador:
            print('Menos... tente novamente.')
print(f'Acertou com {palpites} tentativas parabéns!')
