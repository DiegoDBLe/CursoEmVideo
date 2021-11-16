#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚTIMO NOME SEPARADAMENTE
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Muito Prazer Sr.(a)! ')
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome é {}'.format(nome[len(nome)-1]))
