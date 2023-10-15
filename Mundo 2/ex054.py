from datetime import date
anoatual = date.today().year
maioridade = 0
menoridade = 0
for i in range(7):
    ano = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(i + 1)))
    idade = anoatual - ano
    if idade >= 21:
        maioridade += 1
    elif idade < 21:
        menoridade += 1
print("---" * 20)
print("Observação: A faixa de maioridade usada aqui é de 21 anos")
print(f"O grupo tem {maioridade} pessoas maiores de idade.")
print(f"Também tem {menoridade} pessoas menores de idade.")
    
