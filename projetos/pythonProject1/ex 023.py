num = int(input('Digite um numero de 0 á 9999 : '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('Analisando o número {}'.format(num))
print('Milhar  : {}'.format(m))
print('Centena : {}'.format(c))
print('Dezena  : {}'.format(d))
print('Unidade : {}'.format(u))







#A = str(input('digite um valor de 0 á 9999 :'))
#print('O milhar  é:  {}'.format(A[0]))
#print('A centena é:  {}'.format(A[1]))
#print('A dezena  é:  {}'.format(A[2]))
#print('A unidade é:  {}'.format(A[3]))