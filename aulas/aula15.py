# VARIAVEIS COMPOSTAS(TUPLAS) AS TUPLAS SÃO IMUTAVEIS

lache = ('Hamburguqer', 'suco', 'pizza', 'pudim')
print(lache[2]) # Vai mostrar a piza que está na posição 2
print(lache[0:2])# Vai mostrar Hamburguqer', 'suco' posição de 0 a 2 sendo que só mostra duas posições. Ou seja posição 0 e 1
print(lache[1:]) # Vai mostrar os lanches na posição 1 até o final. Ou seja começando com na posição 1 ignorando a posição 0
print(lache[-1]) # Vai mostrar o ultimo lanche ou seja o pudim. Se for -2  mostra a pizza e assim sucessivamente
print(len(lache)) # Mostra o cumprimento da variavel. Ou seja quantas posições tem a tupla
for c in lache: # Mostrar todos os elementos da variavel lanche.
    print(c)
for pos, comida in enumerate(lache): # Coloca numero para cada elemento da tupla 0 - Hamburgue -  1 - Suco - 2 - Pizza - 3 - Pudim
    print(f'{pos} - {comida}')
for c in range(0, len(lache)): # Coloca numero para cada elemento da tupla 0 - Hamburgue -  1 - Suco - 2 - Pizza - 3 - Pudim. Sem usar o enumerate
    print(f'{c} -> {lache[c]}')
print(sorted(lache)) # Mostra em ordem Alfabetica
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5)) # Método count vai verificar quantas vezes o numero 5 se repete. Nesse exemplo 2x
print(c.index(4)) # Em qual posição está o numero passado em parametro
pessoa = ('Diego', 33, 'M', 121) # Exemplo de tupla que recebe tanto string quanto numero
print(pessoa)
del(pessoa) # apaga tupla, lista, variavel
print(pessoa)

