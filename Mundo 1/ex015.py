km = float(input('Imagine que você alugou um carro, quantos km você rodaria com ele? (1 km = R$0,15) '))
dia = float(input('E por quantos dias você teria alugado ele? (1 dia = R$60) '))
pkm = km * 0.15
pdia = dia * 60
pagamento = pkm + pdia
print('Você teria gastado {} em km rodados e {} em dias usados'.format(pkm, pdia))
print('O total a pagar é {}'.format(pagamento))
