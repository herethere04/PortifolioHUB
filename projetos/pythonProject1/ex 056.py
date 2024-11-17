soma = 0
maior = 0
mulheres = 0
nomevelho = 0
for c in range(1, 5):
    print(f'_______ {c}° PESSOA _______')
    nome = str(input('Nome :')).upper().strip()
    idade = int(input('Idade :'))
    sexo = str(input('Gênero M/F :')).strip().upper()
    soma = (soma + idade)
    media = soma / 4
    if c == 1 and sexo == 'M':
        nomevelho = nome
        maior = idade
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            nomevelho = nome
    if sexo == 'F':
        if idade < 20:
            mulheres = mulheres + 1
print('_________________________')
print('Têm {} mulheres abaixo dos 20 anos'.format(mulheres))
print('A media de idade é {:.1f} anos'.format(media))
print('O homem com maior idade é {} e seu nome é {}'.format(maior, nomevelho))
