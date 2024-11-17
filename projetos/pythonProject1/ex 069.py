print('-'* 20)
print('Cadastre uma pessoa')
print('-'* 20)
idademaior = homens = mulhervinte = 0
while True:
    i = int(input('Idade :'))
    g = ' '
    while g not in 'mf':
        g = str(input('Genero [M/F] :')).strip().lower()[0]
    c = ' '
    while c not in 'sn':
        c = str(input('Quer continuar [S/N] :'))
    if i >= 18:
        idademaior += 1
    if g == 'm':
        homens += 1
    if g == 'm' and i < 20:
        mulhervinte += 1
    if c == 'n':
        break
print(f'Total de pessoas maiores de idade : {idademaior}')
print(f'Total de homens cadastrados : {homens}')
print(f'Total de mulheres com menos de 20 anos : {mulhervinte}')
