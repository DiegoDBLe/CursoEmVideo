# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA: [1] SOMAR, [2] MULTIPLICAR, [3] MAIOR, [4] NOVOS NÚMEROS E [5] SAIR DO PROGRAMA
from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

print('*' * 20)
opcao = ''
while opcao != 5:
    opcao = int(input(
        '[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA \nDigite a Opção Desejada: '))
    if opcao == 1:
        somar = n1 + n2
        print('A Soma entre {} + {} = {}'.format(n1, n2, somar))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A Multiplicação entre {} e {} = {}'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2 or n2 < n1:
            print('O maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    elif opcao == 4:
        n1 = float(input('Digite novos números: '))
        n2 = float(input('Digite novos números: '))
    elif opcao == 5:
        sleep(0.5)
        print('SAINDO...')
    else:
        print('\033[1;31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE.\033[m')
