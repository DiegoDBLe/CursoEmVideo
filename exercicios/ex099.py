# faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros. Seu programa tem que analisar todos os valores
# e dizer qual deles é o maior.
from time import sleep


def maior(* num):

    cont = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        sleep(0.5)
        print(f' {n}', end='')
        cont += 1
    print(f' Foram informados {cont} valores ao todo.')
    print('O maior valor informado foi:', max(num))


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)

# ABAIXO SOLUÇÃO DO PROFESSOR:


def maioR(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores...')
    for n in num:
        sleep(0.5)
        print(f' {n}', end='')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi: {maior}.')


maioR(2, 9, 4, 5, 7, 1)
maioR(4, 7, 0)
maioR(1, 2)
maioR(6)
maioR()

