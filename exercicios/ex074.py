# CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA. DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE
# O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.
from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os numeros sorteados foram: {numero}')
print(f'O Maior numero sorteado foi: {max(numero)}')
print(f'O Menor número sorteado foi: {min(numero)}')
# Ou outra maneira de printar.
print(f'Os numeros sorteados foram: ', end='')
for n in numero:
    print(f'{n} ', end='')
