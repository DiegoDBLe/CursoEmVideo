# LISTAS DENTR4O DE LISTAS. VÁRIAVEIS COMPOSTAS

# CRIANDO UMA LISTA NORMAL
print('LISTA NORMAL')
lista = list()
lista.append('Diego')
lista.append(33)
print(lista)
print('-=-' * 30)
print()

# COLOCANDO UMA LISTA DENTRO DA OUTRA FAZENDO UMA CÓPIA DA LISTA E ADICIONANDO MAIS UM ELEMENTO
print('Adicionando uma lista na outra e colocando um elemento: ')
galera = list() # Criando uma outra lista
galera.append(lista[:]) # adicionando e fazendo uma cópia da lista em galera
lista[0] = 'Levi' # adicionando elemento na primeira lista
lista[1] = 1
galera.append(lista[:]) # adicionando os elementos adicionandos na lista em galera
print(galera)
print('-=-' * 30)
print()

# Outra maneira de colocar uma lista dentro da outra
galera1 = [['Diego', 33], ['Levi', 1], ['Thyci', 33], ['neurimar', 26]]
print(galera1[0]) # Vai printar ['Diego', 33]
print(galera1[0][0]) # vai printar somente Diego
print(galera1[1][0]) # vai printar somente Levi
print(galera1[2][0]) # vai printar somente Thyci
print(galera1) # Vai printar tudo
print('-=-' * 30)
# Varrendo a lista galera atráves do for:
print('Varrendo a lista galera atráves do for: ')
for c in galera1:
    print(f' Mostrando todos: {c}', end='')
print('\n-=-' * 5)
print(f' Mostrando somente o primeiro nome: ')
for c in galera1:
    print(f'- {c[0]}')
print('\n-=-' * 5)
print(f' Mostrando somente a idade: ')
for c in galera1:
    print(f'Idade: {c[1]} ')
print('-=-' * 30)
# SOLICITANDO PRO USUARIO AS INFORMAÇÕES:
galera2 = list()
dado = list()
totMenor = totMaior = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear() # aqui ele apaga as informações de dado e fica somente na lista galera2. Para nãi ficar informação repetida nas duas listas
print(galera2)
print(f'vazio: {dado}') #vazio
print('-=-' * 30)
# MOSTRANDO SOMENTE OS MAIORES DE IDADE DA LISTA(GALERA2):
print('Somente os maiores de idade: ')
for p in galera2:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totMenor += 1
print(f'Temos {totMaior} maiores e {totMenor} menores de idade.')