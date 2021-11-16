#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA SUA PORÇÃO INTEIRA
#EX: DIGITE UM NUMERO: 6.127. O NUMERO TEM A PARTE INTEIRA 6
import math
num = float(input('Digite um numero: '))
print('A parte inteira de {} é {}'.format(num, math.floor(num)))
''' OU '''
print('A parte inteira {} é {}'.format(num, int(num)))
''' OU '''
print('A parte inteira de {} é {}'.format(num, math.trunc(num)))
