sexo = str(input('informe seu sexo [M/F] :')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Resposta invalida, por favor informe seu sexo [M/F] :')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')


'''m = 'M'
f = 'F'
while f == 'F' and m == 'M':
    n = str(input('Qual seu sexo ? [M/F] :')).upper().strip()[0]
    if n != f and n != m:
        print('Resposta invalida, tente novamente!')
    else:
        print('Dados registrados o sucesso!')'''
