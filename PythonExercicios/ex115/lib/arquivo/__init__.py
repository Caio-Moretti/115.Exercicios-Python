from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')
    finally:
        a.close()

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>7} anos')


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at+')
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'Houve um ERRO no cadastro dos dados.')
        else:
            print(f'Novo registro de {nome}')
            a.close()
