aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
print('=' * 50)
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
print(f'O aluno está {aluno["situacao"]}')

