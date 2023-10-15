palavras = ('aprender', 'programar', 'linguagem', 'curso', 'gratis', 'bacanudo', 'mercado', 'paciencia', 'trabalho')
for palv in palavras:
    print(f'A palavra {palv.upper()} tem ', end='')
    for ind, letra in enumerate(palv):
        if letra in 'aeiou':
            print(letra, end=' ')
    print('')
