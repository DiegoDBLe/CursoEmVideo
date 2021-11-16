# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. N
# NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES DESCONSIDERANDO O FLAG
numero = cont = soma = 0
while numero != 999:
    numero = int(input('Digite um número: [999 para parar]: '))
    cont += 1
    soma += numero
print('Você digitou {} números e a soma entre ele foi {}.'.format(cont - 1, soma))

# NESSA SOLUÇÃO DE CIMA TEM UMA GANBIARRA NO CONT - 1 E NÃO CONSIGO SOMAR DESCONSIDERANDO O FLAG.

# NO EXERCICIO ABAIXO TEM UMA MANEIRA DIFERENTE DE FAZER MUITO PARECIDA COM A DE CIMA, NÃO É A IDEAL PORÉM RESOLVE:

cont = soma = 0
numero1 = int(input('Digite um número: [999 para parar]: '))
while numero1 != 999:
    cont += 1
    soma += numero1
    numero1 = int(input('Digite um número: [999 para parar]: '))
print('Você digitou {} números e a soma entre eleS foi {}.'.format(cont, soma))

