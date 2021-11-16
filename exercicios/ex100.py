# FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIOS() E SOMAPAR. A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCA-LOS
# DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR.
from random import randint
from time import sleep
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(valores)


def sorteios(lista):
    print(f'Sorteando 5 valores da lista:', end='')

    for n in lista:
        sleep(0.5)
        print(f' {n}', end='')
    print(' PRONTO!')


def somaPar(lista):
    somaPar = 0
    for n in lista:
        if n % 2 == 0:
            somaPar += n
    print(f'Somando os valores pares da lista: {valores}, temos: {somaPar}')


sorteios(valores)
somaPar(valores)
print()
# ABAIXO SOLUÇÃO DO PROFESSOR:
print()
numeros = list()
def sorteia(listas):
    print('SORTEANDO 5 VALORES DA LISTA: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        listas.append(n)
        sleep(0.3)
        print(f'{n} ', end='')
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares da lista: {lista}, temos {soma}')


sorteia(numeros)
somapar(numeros)
