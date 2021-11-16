# VÁRIAVEIS COMPOSTAS ( DICIONÁRIOS)
# tupla () ---- lista [] ---- dicionário {}
pessoas = {'Nome': 'Diego', 'Sexo': 'Masculino', 'Idade': '33'}
print(pessoas)
print('-=' * 30)
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print('-=' * 30)
for k, v in pessoas.items():
    print(f'{k}: {v}')
print('-=' * 30)
print('Somente as keys(indice) do dicionário: ', pessoas.keys())
print('Somente os valores das Keys do dicionário: ', pessoas.values())
print('-=' * 30)
# APAGANDO UM INDICE:
del pessoas['Sexo']
print('Apagando o indice sexo: ', pessoas)
# ADICIONANDO O INDICE SEXO:
pessoas['Sexo'] = 'M'
print('Adicionando o indice sexo: ', pessoas)
print('-=' * 30)
# MUDANDO O VALOR DO INDICE:
pessoas['Nome'] = 'Levi'
print('Mudando o nome de Diego para Levi: ', pessoas)
pessoas['Nome'] = 'Diego'
pessoas['Peso'] = '122 Kgs'
print('Adicionando o peso: ', pessoas)
print('-=' * 30)
print('-=' * 30)
print('-=' * 30)
print(' '*10, 'CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA', ' '*10)
print('-=' * 30)
# Criando uma lista chamada de Brasil
# Adicionando os estados no dicionário
# Brasil é uma lista e estado1 e estado2 dicionários
# Adicionando os dicionários na lista
brasil = []
estado1 = {'UF': 'Ceará', 'Sigla': 'Ce', 'Capital': 'Fortaleza'}
estado2 = {'UF': 'Paraiba', 'Sigla': 'PB', 'Capital': 'João Pessoa'}
brasil.append(estado1)
brasil.append(estado2)

print('Mostrando a lista com os dicionários: ', brasil)
print('Mostrando o indice 0 da minha lista: ', brasil[0])
print('Mostrando o indice 1 da minha lista: ', brasil[1])
print('Mostrando a capital do ceará: ', brasil[0]['Capital'])
print('Mostrando a sigla da Paraiba: ', brasil[1]['Sigla'])
print('-=' * 30)
print('-=' * 30)

estado = dict() # Dicionário
brasil1 = list() # Lista
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil1.append(estado.copy()) # Cópia da lista
for e in brasil1: # for na lista, vai mostrar dicionario de cada estado.
    for k, v in e.items(): # for no dicionario. esse e é referente ao estado (e) do outro for
        print(f'{k}: {v}', end=' ')
    












