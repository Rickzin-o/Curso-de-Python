valor = n = int(input('Sequência de Fibonacci! Quantos termos você quer ver? '))
sequencia = [0, 1]
n -= 2
while n > 0:
    novovalor = sequencia[-1] + sequencia[-2]
    sequencia.append(novovalor)
    n -= 1
print(f'Os {valor} primeiros números da sequência fibonacci são {sequencia[:valor]}')
