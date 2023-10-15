def fatorial(num, show=False):
    """
Calcula o fatorial de um número.
:param num: O número que terá a fatorial calculada.
:param show: Valor booleano para mostrar o cálculo.
:return: Valor da fatorial do número.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            s = f'{i} =' if i == 1 else f'{i} x'
            print(s, end=' ')
    return f

print(fatorial(5, True))
