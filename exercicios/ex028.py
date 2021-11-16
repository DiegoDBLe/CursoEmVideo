# CRIE UM PROGRAMA NA TELA QUE LEIA UM NUMERO E DIGA SE ELE É PAR OU IMPAR
numero = int(input('Digite um numero para saber se é PAR ou IMPAR: '))
if numero % 2 == 0:
    print('O numero: {} é PAR'.format(numero))
else:
    print('O numero: {} é IMPAR'.format(numero))
