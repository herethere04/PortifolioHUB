def valor_absoluto(numero):
    if numero < 0:
        return - numero
    else:
        return numero

def main():
    numero = float(input("Digite um número: "))
    resultado = valor_absoluto(numero)
    print(f"O valor absoluto é: {resultado}")

main()
