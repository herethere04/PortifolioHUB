casa = float(input('Valor da casa ?'))
salario = float(input('Qual seu salario mensal ?'))
ano = int(input('Em quantos anos irá pagar ?'))
parcela = casa // (ano * 12)
if parcela <= salario * 0.30 :
    print('Parabens seu emprestimo foi aprovado')
else :
    print('infelizmente a parcela de {:.2f} ficará maior que 30 % de seu salario q é {:.2f} portanto n será aprovado'.format(parcela,salario * 0.30))