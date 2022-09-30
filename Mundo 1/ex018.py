import math
angulo = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Esse ângulo tem o Seno de {:.2f}, o Cosseno de {:.2f} e a Tangente de {:.2f}'.format(seno, cosseno, tangente))