#CRIE UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MULTIPLOS DE 3 E QUE SE ENCONTRAM ENTRE 1 ATÉ 500
s = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c #Esse soma
        cont += 1 # Esse conta
print('Somando todos os {} valore  impares fica no total de {}'.format(cont, s))
