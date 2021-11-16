import math
import random

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
#math.cail(raiz) Arredonda pra cima
#math.floor(raiz) Arredonda pra baixo
# PARA SABER TODAS AS IMPORTAÇÕES QUE PODE SER FEITA NO PHYTON VAI EM python.org > docs > Library reference > lista de modulos(bibliotecas)
# EM PYPI TEM A LISTA DE PACOTES EXTRAS

# Computador gera numeros aleatorios
num1 = random.randint(1,50)
print(num1)


