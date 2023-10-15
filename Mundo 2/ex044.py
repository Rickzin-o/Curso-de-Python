print('=-=' * 10)
print('\033[0:36mVocê vai comprar um produto...\033[m')
print('=-=' * 10)
produto = float(input('Digite o preço do produto: R$'))
fdepag = int(input("""Qual a forma de pagamento? Digite:
1 - Para pagamento à vista com dinheiro ou cheque
2 - Para pagamento à vista com cartão
3 - Para pagamento parcelado em até 2x no cartão
4 - Para pagamento parcelado em 3x ou mais no cartão
Digite o número: """))
p4 = (produto / 100) * 20 + produto
p1 = produto - (produto / 100) * 10
p2 = produto - (produto / 100) * 5
if fdepag == 1:
    print('Com essa forma de pagamento você tem 10% de desconto, logo você paga R${:.2f}'.format(p1))
elif fdepag == 2:
    print('Com essa forma de pagamento você tem 5% de desconto, logo você paga R${:.2f}'.format(p2))
elif fdepag == 3:
    print('Com essa forma de pagamento você não recebe juros, logo paga R${:.2f} por parcela'.format(produto / 2))
else:
    parcelas = int(input('Quantas parcelas? '))
    print('Com essa forma de pagamento você recebe 20% de juros, e o preço fica em {}x de R${:.2f}'.format(parcelas, p4 / parcelas))
    print('O preço total é de R${}'.format(p4))
