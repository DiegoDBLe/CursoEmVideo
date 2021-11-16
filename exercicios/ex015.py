#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CAULCULE E MOSTRE O COMPRIMENTO DO HIPOTENUSA
import math
'''Mnaira importando a biblioteca Math'''
catetOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o compimento do cateto adjacente: '))
hipotenusa = math.hypot(catetOposto, catetoAdjacente)
print('A hipotenussa vai medir {:.2f}'.format(hipotenusa))



'''Maneira tradicional de fazer o calculo.'''
# catetOposto = float(input('Digite o comprimento do cateto oposto: '))
# catetoAdjacente = float(input('Digite o compimento do cateto adjacente: '))
# hipotenusa = (catetOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
# print('A hipotenussa vai medir {:.2f}'.format(hipotenusa))
