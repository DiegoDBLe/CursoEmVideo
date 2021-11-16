# Formatação padrão
nome = input('Qual seu nome? ')
print('Prazer em conhecer Sr. {}!'.format(nome))

#Alinhado a 20 posições ou seja a ! ficou 20 caracteres depois do nome
nome = input('Qual seu nome? ')
print('Prazer em conhecer Sr. {:20}!'.format(nome))

# Colocando o nome para direita em 20 posições
nome = input('Qual seu nome? ')
print('Prazer em conhecer Sr. {:>20}!'.format(nome))

# Colocando o nome para esquerda em 20 posições
nome = input('Qual seu nome? ')
print('Prazer em conhecer Sr. {:<20}!'.format(nome))

# Centralizando
nome = input('Qual seu nome? ')
print('Prazer em conhecer Sr. {:^20}!'.format(nome))

# Centralizando e separando por caracteres
nome = input('Qual seu nome? ')
print(f'Prazer em conhecer Sr. {nome:=^20}!')

