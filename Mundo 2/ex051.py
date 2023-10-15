pa = []
print("Hora da Progressão Aritmética!")
primterm = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = (primterm + (10 - 1) * razao) + razao
for i in range(primterm, decimo, razao):
    print(i, end=', ')
print('fim.')
