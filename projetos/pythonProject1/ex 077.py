palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print(f'Vogais da palavra {palavra}: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(f'\033[1;33m{letra.lower()}\033[m', end=' ')
    print()


