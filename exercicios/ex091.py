# CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSES RESULTADOS EM UM DICIONÁRIO. NO FINAL, COLOQUE ESSE
# DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO.
from random import randint
from time import sleep
from operator import itemgetter
ranking = {}
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(2)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)

