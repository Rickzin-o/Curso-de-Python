idades = []
generos = []
maisvelho = 0
nomemaisvelho = ''
for i in range(4):
    print(f"{i+1}ª pessoa")
    nome = str(input("Digite o nome: ")).strip()
    idade = int(input("Digite a idade: "))
    idades.append(idade)
    sexo = str(input("Digite o sexo (M/F): ")).strip()
    generos.append(sexo)
    if i == 0 and sexo in "Mm":
        maisvelho = idade
        nomemaisvelho = nome
    elif sexo in "Mm" and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    print("--" * 40)
mediaidades = (idades[0] + idades[1] + idades [2] + idades[3]) / 4
print(f"A média de idades é {mediaidades} anos.")
mulheres = 0
for i in range(4):
    if generos[i] in "Ff" and idades[i] < 20:
        mulheres += 1
print("O grupo tem {} mulheres com menos de 20 anos.".format(mulheres))
print(f"O nome do homem mais velho é {nomemaisvelho}.")
