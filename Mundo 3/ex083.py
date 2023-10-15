express = str(input('Crie uma expressão matemática: '))
lista = []
for carac in express:
    if carac == '(':
        lista.append(carac)
    elif carac == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(carac)
            break

if len(lista) > 0:
    print('Essa expressão é inválida!')
elif len(lista) == 0:
    print('Essa expressão é válida.')
