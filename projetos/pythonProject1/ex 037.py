n = int(input('Diga um numero inteiro :'))
n1 = (input('digite 1 para binario, 2 para octal e 3 para hexadecimal:'))
if n1 == 1 :
    print('O numero {}, em binario fica {}'.format(n,bin(n)[2:]))
elif n1 == 2:
    print('O numero {}, em octal fica {}'.format(n,oct(n)[2:]))
elif n1 == 3:
    print('o numero {}, em hexadecimal fica {}'.format(n,hex(n)[2:]))
else :
    print('Opção inválida tente novamente')