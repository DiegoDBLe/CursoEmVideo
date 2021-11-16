# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE
# A MÉDIA DE IDADE DO GRUPO, QUAL O HOMEN MAIS VELHO, QUANTAS MULHERES TEM MENOS DE 20 ANOS.
s = 0
maioridadeHomem = 0
nomeVelho = ''
mulher = 0
for c in range(0+1, 4+1):
    nome = str(input('Digite Seu nome: ')).strip()
    idade = float(input('Digite sua Idade: '))
    sexo = str(input('Qual seu sexo? [F]-[M]: ')).strip().upper()
    print('=*' * 25)
    s += idade
    if c == 1 and sexo in 'Mn': # Substitui o upper o usuario pode digitar tanto minusculo quanto maiusculo que ele reconhece
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mn' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
mediaGrupo = s / 4
if maioridadeHomem == 0:
    print('NÃO FOI DIGITADO NENHUM HOMEN ')
else:
    print('O Homem mais velho tem {} anos e se chama {}'.format(maioridadeHomem, nomeVelho))
print('A média de idade do grupo é de {:.2f} anos'.format(mediaGrupo))
if mulher == 1:
    print('Tem {} mulher abaixo de 20 anos'.format(mulher))
else:
    print('Tem {} mulheres abaixo de 20 anos'.format(mulher))

