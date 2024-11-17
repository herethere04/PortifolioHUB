p = int(input('Qual o primeiro termo ?'))
r = int(input('Qual a razão ?'))
c = 0
valor = p + r
while c != 10:
    print(valor, end=' ')
    c = c + 1
    valor = valor + r
