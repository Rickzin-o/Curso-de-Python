extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número inteiro entre 0 e 20: '))
while not 0 <= n <= 20:
    n = int(input('Erro! Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[n].lower()}')
