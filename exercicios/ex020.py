# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# O NOME COM TODAS AS LETRAS MAIUSCULA
# O NOME COM TODAS AS LETRAS MINUSCULA
# QUANTAS LETRAS AO TODO SEM CONSIDERAR OS ESPAÇOS
# QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite seu nome completo: ')).strip() #Elimina os espaços antes do nome e depois
print('Seu nome em maiusculo fica: ', nome.upper(),
      '\n Em Minusculo fica:', nome.lower(),
      '\n Quantas letras tem o nome:', len(nome) - nome.count(' '),
      '\n Quantas letras tem o primeiro nome:', nome.find(' '))
