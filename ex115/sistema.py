from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

# Criando uma variavel que recebe o nome do arquivo:
arquivo = 'cursoemvideo.txt'

# Saber se arquivo existe: se não existir ele vai criar atraves da função criar arquivo.
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo.
        lerArquivo(arquivo)
    elif resposta == 2:
        #opção para cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().capitalize()
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, sexo, idade)
    elif resposta == 3:
        corVermelho('Saindo do Sistema...')
        sleep(2)
        corAmarelo('Até Logo e Volte Sempre!')
        break
    else:
        corVermelho('ERRO! Digite uma opção válida!')
    sleep(2)
