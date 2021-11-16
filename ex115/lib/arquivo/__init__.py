# Criando um método para abrir arquivo, fechar e saber se existe:
from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt modo de leitura
        a.close()
    except FileNotFoundError:  # se retornar um erro de n ão encontrado ele vai retornar false
        return False
    else:
        return True


# Função para criar um arquivo
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #variavel para criar o arquivo. w = write ou seja escreva, t = de text sinal de + é se não tiver crie
        a.close()
    except:
        corVermelho('Houve um erro na criação do arquivo!')
    else:
        corVerde(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        corVermelho('Erro ao ler o aqruivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<15}sexo:{dado[1]} idade:{dado[2]} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', sexo='Não informado', idade=0):
    try:
        a = open(arquivo, 'at') # a de append ou seja de adicionar.
    except:
        corVermelho('Houve um ERRO na abertura do aqruivo!')
    else:
        try:
            a.write(f'{nome}; {sexo}; {idade}\n')
        except:
            corVermelho('Houe um ERRO na hora de escrever os dados!')
        else:
            corVerde(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()


