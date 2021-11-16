# CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR QUER OU NÃO CONTINUAR, SE O USUARIO QUISER
# NO FINAL MOSTRE: A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS; B) QUANTOS HOMENS FORAM CADASTRADOS; C) QUANTAS MULHERES TEM MENOS DE 20 ANOS:
print('-' * 40)
print('CADASTRE UMA PESSOA')
print('-' * 40)
contador = contadorHomens = contadorMulher = 0
print('-' * 40)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 40)
    continuar = str(input('Quer continuar? [S/N] : ')).strip().upper()[0]
    if idade >= 18:
        contador += 1
    if sexo in 'Mm':
        contadorHomens += 1
    elif sexo in 'Ff' and idade <= 20:
        contadorMulher += 1
    if continuar in 'Nn':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {contador}\nAo todo temos {contadorHomens} homens cadastrados, \nE temos {contadorMulher} melheres com menos de 20 anos')

#SOLUÇÃO DO PROFESSOR ABAIXO:
# contador = contadorHomens = contadorMulher = 0
# while True:
#  idade = int(input('Idade: '))
#  sexo = ' '
#   while sexo not in 'MF':
#           sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
#   if idade >= 18:
#         contador += 1
#   if sexo == 'M':
#         contadorHomens += 1
#   elif sexo == 'F' and idade <= 20:
#         contadorMulher += 1
#   resp = ' '
#   while resp not in 'SN':
#       resp = str(input('Quer continuar? [S/N] : ')).strip().upper()[0]
#   if resp == 'N':
#       break
