# LISTAS: SÃO MUTÁVEIS
#Criando uma Lista com 4 elementos:
lista = [2, 5, 9, 7]
print(f'Criando uma Lista: {lista}')
# Modificando um elemento especifico da lista no exemplo mudando o 9 por 3:
lista[2] = 3
print(f'Modificando um elemento especifico da lista: {lista}')
# Adicionando um elemento na lista
lista.append(7)
print(f'Adicionando um elemento na lista: {lista}')
# Colocando os elementos da lista em ordem:
lista.sort()
print(f'Colocando os elementos da lista em ordem: {lista}')
# Colocando os elementos da lista em ordem reversa:
lista.sort(reverse=True)
print(f'Colocando os elementos da lista em ordem reversa: {lista}')
# Inserindo elemento na lista na posição que eu escolher: (posição, elemento que desejo inserir)
lista.insert(2, 4)
print(f'Inserindo elemento na lista na posição que eu escolher: {lista}')
# Remover o elemento escolhido:
if 7 in lista:
    lista.remove(7)
else:
    print('Não achei o numero 7 na lista.')
lista.sort()
print(f'Remover o elemento escolhido: {lista}')
# Saber quantos elementos tem a lista:
print(f'Essa lista tem {len(lista)} elementos')
print('*=-' * 90)
print('*=-' * 90)
print('*=-' * 90)
print('*=-' * 90)
# Posso criar uma lista vazia assim ou assim:
# Posso passar os valores ja na declaração ou adicionando depois
#valores = list()
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valore {v}!')
print('Cheguei ao final da lista.')

# Adicionando numeros na lista lidos pelo teclado:
numeros = []
for cont in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
for c, v in enumerate(numeros):
    print(f'Na posição {c} encontrei o número {v}')
print('Acabou.....')
print('*=-' * 90)
print('*=-' * 90)
print('*=-' * 90)
print('*=-' * 90)
# Quando eu digo que 'b' recebe 'a' qualquer elemento que eu adicione ou altere em 'b' a lista 'a' tbm será alterada
# Pytohn faz a ligação de uma lista com a outra.
a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a} \nLista B: {b}')
b.append(5)
print(f'Lista A: {a} \nLista B: {b}')
# Após adicionar o 5 na lista 'b' lista 'a' tbm foi adicionado o número 5.
# Para que isso não aconteça ou seja que seja criada uma cópia de outra lista é necessario fazer da seguinte forma:
b = a[:]
b.append(1)
print(f'Lista A: {a} \nLista B: {b}')
# Foi feito uma cópia da Lista 'a' e adicionando ellemnto na lista 'b' sem alterar lista 'a'
