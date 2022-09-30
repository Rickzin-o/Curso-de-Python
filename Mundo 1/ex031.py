km = float(input('Quantos quilômetros tem sua viagem de ônibus? '))
p1 = km * 0.50 # Valor para a primeira condição
p2 = km * 0.45 # Valor para a segunda condição
if km <= 200:
    print('Você paga R$0,50 cada km se sua viagem for de até 200km\nLogo você paga R${:.2f}'.format(p1))
else:
    print('Você paga R$0,45 cada km se sua viagem for maior que 200km\nLogo você paga R${:.2f}'.format(p2))
