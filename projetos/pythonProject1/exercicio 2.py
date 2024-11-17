def positivo_nulo_negativo(numero):
    if numero > 0:
        print("Valor Positivo")
    elif numero == 0:
        print("Valor Nulo")
    else:
        print("Valor Negativo")

def main():
    numero = float(input("Digite um número: "))
    positivo_nulo_negativo(numero)

main()
