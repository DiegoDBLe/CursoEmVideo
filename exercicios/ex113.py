# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mDigite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mO Usúario prefere não digitar esse número.')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
num1 = leiaFloat('Digite um número real: ')
print(f'O valor digitado foi {num} e o valor real foi {num1}')