import math
co = float(input('Digite o valor de um cateto oposto de um triângulo: '))
ca = float(input('Agora digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa desse triângulo tem o valor de {:.2f}'.format(h))
