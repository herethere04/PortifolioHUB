lista = []
while True:
    v = int(input('Digite um valor :'))
    if v not in lista:
        lista.append(v)
    else:
        print('Esse número já está na lista, n será adicionado.')
    r = str(input('Quer continuar adicionando ? (S/N) : ')).lower().strip()
    if r == 'n':
        break
    while r not in 'sn':
        r = str(input('Quer continuar adicionando ? (S/N) : ')).lower().strip()
        if r == 'n':
            break
print(sorted(lista))
