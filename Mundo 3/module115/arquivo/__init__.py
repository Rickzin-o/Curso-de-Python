def fileexist(file):
    try:
        a = open(file, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criararquivo(file):
    try:
        a = open(file, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo')


def fileread(file):
    try:
        with open(file, 'rt') as f:
            a = f.read()
            return a
    except:
        print(f"ERRO! Não foi possível abrir '{file}'")


def filewrite(file, text):
    try:
        with open(file, 'at') as f:
            f.write(text)
    except:
        print('Algo deu errado.')
