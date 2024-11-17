v = float(input('Qual o valor da compra :'))
print('''[ 1 ] Para pagamento á vista em dinheiro / cheque
[ 2 ] Para pagamento á vista no cartão
[ 3 ] Para pagamento em até 2x no cartão
[ 4 ] Para pagamento em 3x ou mais no cartão''')
n = int(input('Qual opção : '))
if n == 1:
    print('Pagando á vista no dinheiro / cheque vc ganha 10% de desconto portanto sua compra ficou R${:.2f}'.format(v * 0.90))
elif n == 2:
    print('Pagando á vista no cartão vc ganha 5% de desconto portanto sua compra ficou R${}'.format(v * 0.95))
elif n == 3:
    print(f'Pagando em até 2x no cartão o preço permaneçe R${v}')
elif n == 4:
    juros = v * 1.20
    parcelas = int(input('Quantas parcelas ? '))
    print('Sua compra de R${:.2f} ficou R${:.2f} devido aos juros, com parcelas de R${:.2f}'.format(v,juros,juros / parcelas))
else:
    print('Não existe essa opção, tente novamente.')