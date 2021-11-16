# Criando um método para definição das linhas do cabeçalhho. Onde o padrão é 42 se eu não passar nada no parametro.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por Favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsúario preferiu não digitar nenhum número.')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


# Criadno um método para definição de cabeçalho: que tem uma linha em cima o texto no meio e outra linha embaixo.
def cabecalho(txt):
    print(linha())
    corVerde(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33;1m{c}\033[m - \033[34;1m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32;1mDigite sua opção:\033[m ')
    return opc


def corVermelho(vermelho):
   print(f'\033[31;1m {vermelho}\033[m')


def corAmarelo(amarelo):
    print(f'\033[33;1m{amarelo}\033[m')


def corAzul(azul):
    print(f'\033[34;1m{azul}\033[m')


def corVerde(verde):
    print(f'\033[32;1m{verde}\033[m ')

