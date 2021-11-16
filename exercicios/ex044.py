# FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO, INICIANDO DE 10 ATÉ 0 ENTRE ELES
from time import sleep
print('-=-' * 8)
print('CONTAGEM REGRESSIVA...')
print('-=-' * 8)
for c in range(10, 0-1, -1):
    sleep(1)
    print(c)
print('\033[1;32mFELIZ ANO NOVO!!!\033[m', '\033[1;32m*\033[m' * 25)
