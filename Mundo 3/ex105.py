def notas(*num, sit=False):
    """
Coleta notas de vários alunos e as analisa.
:param num: Notas dos alunos
:param sit: Valor opcional para indicar se a situação pode ser colocada na análise
:return: Dicionário com a análise
"""
    dicio = {'total': len(num), 'maior': max(num), 'menor': min(num),
             'média': (sum(num)/len(num))}
    if sit:
        m = dicio['média']
        if m >= 7:
            dicio['situação'] = 'BOA'
        elif 5 <= m < 7:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio

print(notas(4.5, 9.5, 5, 7.5, 3, 6, 7, sit=True))
help(notas)
