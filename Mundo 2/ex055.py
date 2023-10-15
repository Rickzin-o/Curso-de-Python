maior = 0
menor = 0
for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso é de {maior}KG")
print(f"O menor peso é de {menor}KG")
