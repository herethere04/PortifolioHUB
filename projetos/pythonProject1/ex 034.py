salario = float(input('Qual os seu salario ?'))
aumento1 = salario * 1.10
aumento2 = salario * 1.15
if salario <= 1250 :
    print('O seu salario de {:.2f} com o aumento de 15% vai ficar {:.2f}'.format(salario ,aumento2 ))
else :
    print('O seu salario de {:.2f} com o aumento de 10% via ficar {:.2f}'.format(salario ,aumento1 ))