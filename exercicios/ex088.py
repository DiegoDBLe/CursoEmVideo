# FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR UM PALPITE. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E
# VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UM LISTA COMPOSTA:
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('     JOGOS DA MEGA SENA      ')
print('-' * 30)
quantidadeJogos = int(input('Quantos jogos vou sortear? '))
totjogos = 1
while totjogos <= quantidadeJogos:
    contNumeros = 0
    while True:
        sortear = randint(1, 60)
        if sortear not in lista:
            lista.append(sortear)
            contNumeros += 1
        if contNumeros >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totjogos += 1
print('-=' * 30)
print(f'     SORTEANDO {quantidadeJogos} JOGOS')
print('-=' * 30)
for i, l in enumerate(jogos):
    print(f'{i+1}° Jogo: {l}')
    sleep(1)
print('-=' * 5, '= BOA SORTE! =', '-=' * 5)

