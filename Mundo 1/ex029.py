velocidade = float(input('Digite uma velocidade em km/h: ')) # A velocidade do carro para o programa
multa = (velocidade - 80) * 7 # Uma multa de 7 reais a cada quilômetro acima de 80
if velocidade > 80:
    print('Opa! Parece que você passou do limite de velocidade de 80km/h! Sua multa foi de R${:.2f}'.format(multa))
else:
    print('Sua velocidade está dentro dos limites, continue assim!')
print('Boa viagem!')
