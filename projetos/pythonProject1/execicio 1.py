def maximo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    resultado = maximo(numero1, numero2)
    print(f"O maior número é: {resultado}")

main()
