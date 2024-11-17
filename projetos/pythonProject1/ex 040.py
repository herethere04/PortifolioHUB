n1 = float(input('nota 1 :'))
n2 = float(input('nota 2 :'))
media = (n1 + n2) / 2
if media < 5 :
    print(f'A sua media foi {media} portanto está REPROVADO.')
elif media <= 6.9 :
    print(f'A sua media foi {media} portanto está de RECUPERAÇÃO.')
else :
    print(f'Sua media foi {media} portanto está APROVADO.')