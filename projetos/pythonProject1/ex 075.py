'''v1 = int(input('Digite um valor : '))
v2 = int(input('Digite um valor : '))
v3 = int(input('Digite um valor : '))
v4 = int(input('Digite um valor : '))
v = (v1, v2, v3, v4)
a = v.count(9)
print(v)
print(f'A) O nove apareceu {a} vezes.')
if 3 in v:
    b = v.index(3)
    print(f'B) O primeiro numero 3 aparece na posição {b + 1}')
else:
    print('B) N possui nenhum 3')
print('C) Os numeros pares foram : ',end ='')
if v1 % 2 == 0:
    print(v1, end=' ')
if v2 % 2 == 0:
    print(v2, end=' ')
if v3 % 2 == 0:
    print(v3, end=' ')
if v4 % 2 == 0:
    print(v4, end=' ')'''
# de cima é o meu q usou o v1,2,3,4 pra fazer, e o de baixo é o do prof q usou tupla em tudo


num = (int(input('Digite um numero : ')),
        int(input('Digite um numero : ')),
        int(input('Digite um numero : ')),
        int(input('Digite um numero : ')))
print(f'Vc digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição')
else:
    print('O valor 3 n foi digitado')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')