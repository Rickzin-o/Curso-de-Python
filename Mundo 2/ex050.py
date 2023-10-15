soma = 0
contador = 0
for i in range(6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        contador += 1
        soma += n
print(f"As somas dos {contador} números pares é {soma}")
