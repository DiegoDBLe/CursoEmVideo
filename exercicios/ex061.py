# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELA OS PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE FIBONACCI
print('-' * 30)
print('-- SEQUÊNCIA DE FIBONACCI --')
print('-' * 30)
numero = int(input('Digite um número para saber a sequência: '))
print('~' * 30)
t1 = 0
t2 = 1
print('-> {} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')
print('~' * 30)
