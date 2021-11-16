# CRIE UM PROGRAMA QUE FAZ O COMÚTADOR JOGAR JOKENPÔ COM VOCÊ.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual a Sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('-=-' * 11)

print('-=-' * 20)
print('Computador jogou {}.'.format(itens[computador]))
print('Você jogou {}.'.format(itens[jogador]))
print('-=-' * 20)

if computador == 0:
    if jogador == 0:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32mPARABÉNS!! VOCÊ VENCEU\033[m: {} ganha de {}'.format(itens[1], itens[0]))
    elif jogador == 2:
        print('\033[1;31mVOCÊ PERDEU!!\033[m {} ganha de {}'.format(itens[0], itens[2]))

elif computador == 1:
    if jogador == 0:
        print('\033[1;31mVOCÊ PERDEU!!\033[m {} ganha de {}'.format(itens[1], itens[0]))
    elif jogador == 1:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;32mPARABÉNS!! VOCÊ VENCEU\033[m: {} ganha de {}'.format(itens[2], itens[1]))

elif computador == 2:
    if jogador == 0:
        print('\033[1;32mPARABÉNS!! VOCÊ VENCEU\033[m: {} ganha de {}'.format(itens[0], itens[2]))
    elif jogador == 1:
        print('\033[1;31mVOCÊ PERDEU!!\033[m {} ganha de {}'.format(itens[2], itens[1]))
    elif jogador == 2:
        print('\033[1;33mEMPATE\033[m')

