n1 = int(input('Valor 1 : '))
n2 = int(input('Valor 2 : '))
n3 = int(input('Valor 3 : '))
if n1 > n2 and n1 > n3 :
    print(f'{n1} é o maior')
if n2 > n1 and n2 > n3 :
    print(f'{n2} é maior')
if n3 > n1 and n3 > n2 :
    print(f'{n3} é o maior')

if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor')
if n2 < n1 and n2 < n3:
    print(f'{n2} é menor')
if n3 < n1 and n3 < n2:
    print(f'{n3} é o menor')