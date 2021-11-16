# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL MOSTRE QUANTAS AINDA NÃO ATIGIRAM A MAIOR IDADE E QUANTAS JÁ SÃO MAIORES:
from datetime import date
contador = 0
menor = 0
atual = date.today().year
for c in range(0+1, 7+1):
    anoNascimento = int(input('\nDigite o ano de nascimento do {}° : '.format(c)))
    idade = atual - anoNascimento

    if idade >= 21:
        contador += 1
    else:
        menor += 1

print('\nTem \033[1;32m{} pessoas MAIORES\033[m de idade!'.format(contador))
print(' Tem \033[1;31m{} pessoas MENOR de idade!\033[m'.format(menor))
