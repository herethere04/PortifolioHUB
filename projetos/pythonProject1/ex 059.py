from time import sleep
n1 = int(input('valor 1 :'))
n2 = int(input('valor 2 :'))
escolha = 0
while escolha != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    escolha = int(input('Escolha a operação :'))
    if escolha == 1:
        print('A soma de {} + {} é {}'.format(n1, n2,n1 + n2))
        sleep(1)
    elif escolha == 2:
        print('A multiplicação de {} * {} é {}'.format(n1, n2, n1 * n2))
        sleep(1)
    elif escolha == 3:
        if n1 > n2:
            print('O {} é maior q {}'.format(n1, n2))
            sleep(1)
        elif n2 > n1:
            print('O {} é maior q {}'.format(n2, n1))
            sleep(1)
        else:
            print('Os numeros têm o mesmo valor')
            sleep(1)
    elif escolha == 4:
        n1 = int(input('valor 1 :'))
        n2 = int(input('valor 2 :'))
    elif escolha == 5:
        print('Fim da operação!')
    else:
        print('Escolha inválida tente novamente')
