valor = int(input('Digite um valor para calcular o fatorial: '))
fatorial = 1
while valor != 1:
    fatorial *= valor
    valor -= 1
print(f'O cálculo {valor}! = {fatorial}')
