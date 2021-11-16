from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('     JOGOS DA LOTOFACIL      ')
print('-' * 30)
quantosJogos = int(input('Quantos jogos quer sortear? '))
contJogos = 1
while contJogos <= quantosJogos:
    contNumeros = 0
    while True:
        sortear = randint(1, 25)
        if sortear not in lista:
            lista.append(sortear)
            contNumeros += 1
        if contNumeros >= 15:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    contJogos += 1
print('-=' * 30)
print(f'    SORTEANDO {quantosJogos} JOGOS       ')
print('-=' * 30)
for i, l in enumerate(jogos):
    print(f'{i+1}° Jogo: {l}')
    sleep(1)
print('-=' * 5, '- BOA SORTE! -', '=-' *5)