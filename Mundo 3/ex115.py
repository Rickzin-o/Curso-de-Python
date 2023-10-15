from module115.interface import *
from module115.arquivo import *


file = 'cadastro.txt'
if not fileexist(file):
    criararquivo(file)

while True:
    menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Fechar sistema"])
    escolha = leiaint('Sua opção: ')
    if escolha not in (1, 2, 3):
        print('ERRO! Opção inválida.')
        escolha = 0
        continue

    if escolha == 1:
        linhas('PESSOAS CADASTRADAS', 50)
        try:
            content = fileread(file)
            cadastros = content.split('\n')
            for cad in cadastros[:-1]:
                dado = cad.split(':')
                print(f'{dado[0].ljust(40)}{dado[-1]} anos')
            sleep(1)
        except:
            print('ERRO: Não foi possível abrir cadastros')

    if escolha == 2:
        linhas('NOVO CADASTRO', 50)
        nome = input('Nome: ').strip()
        idade = leiaint('Idade: ')
        pessoa = f'{nome}:{str(idade)}\n'
        try:
            filewrite(file, pessoa)
        except:
            print('ERRO!')
        else:
            print(f'{nome} foi cadastrado(a) no sistema com sucesso!')

    if escolha == 3:
        linhas('Saindo do sistema... Até mais!', 50)
        break
