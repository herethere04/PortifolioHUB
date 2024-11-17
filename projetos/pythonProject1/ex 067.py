cont = 0
n = int(input('Quer ver a tabuada de qual valor ?'))
while True:
    cont += 1
    soma = n * cont
    print(f'{n} x {cont} = {soma}')
    if cont == 10:
        cont = 0
        n = int(input('Quer ver a tabuada de qual valor ?'))
        if n < 0:
            break
        cont += 1
        soma = n * cont
        print(f'{n} x {cont} = {soma}')

