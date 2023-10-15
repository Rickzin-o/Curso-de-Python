l = []
for i in range(5):
    valor = int(input('Digite um número: '))
    if i == 0 or valor > l[-1]:
        l.append(valor)
        print('Número adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(l):
            if valor <= l[pos]:
                l.insert(pos, valor)
                print(f'Número adicionado na posição {pos} da lista.')
                break
            pos += 1
print('--' * 25)
print(f'Os valores digitados, em ordem, foram: {l}')
