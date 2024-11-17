p = int(input('Qual o primeiro termo ?'))
r = int(input('Qual a razão ?'))
t = r
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(t), end=' ')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar a mais ?'))
print(f'Progressão finalizada com {total} termos mostrados')