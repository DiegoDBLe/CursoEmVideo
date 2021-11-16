# ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS MOSTRANDO NA TELA UMA MENSAGEM:
# O PRIMEIRO NUMERO É MAIOR, O SEGUNDO NUMERO É MAIOR, NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O Primeiro numero é \033[1;32mMAIOR!\033[m')
elif n2 > n1:
    print('O Segundo numero é \033[1;32mMAIOR!\033[m')
elif n1 == n2:
    print('\033[1;31mNÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS!\033[m')
