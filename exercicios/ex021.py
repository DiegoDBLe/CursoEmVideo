#FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 ATE 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS
#UNIDADE, CENTENA, DEZENA E MILHAR
import math

numero = int(input('Digite um numero entre 0 e 9999: '))
# print('Unidade: ', numero[3])
# print('Dezena: ',  numero[2])
# print('Centena: ', numero[1])
# print('Milhar',    numero[0])

# OU
unidade = numero // 1 % 10
dezena  = numero // 10 % 10
centena = numero // 100 % 10
milhar  = numero // 1000 % 10

print('Analisando o numero {}'.format(numero))
print('Unidade {}'.format(unidade))
print('Dezena  {}'.format(dezena))
print('Centena {}'.format(centena))
print('Milhar {}' .format(milhar))
