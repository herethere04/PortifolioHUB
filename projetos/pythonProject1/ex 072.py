ex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
, 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = ' '
while n not in '1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20':
    n = str(input('Digite um valor entre 0 e 20: '))
n1 = int(n)
print(f'Voçê digitou o número {ex[n1]}')



#while True:
#    num = int(input('Digite um numero entre 0 e 20:'))
#    if 0 <= num <= 20:
#       break

#isso em cima é pra n fazer aquele trambolho ali em cima