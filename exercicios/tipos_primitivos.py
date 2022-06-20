'''Crie um programa que eia dois números e mostre a soma entre eles: '''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale: {s}')
print()
print()
'''Crie um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ela'''
d = input('Digite algo: ')
print(f'É do tipo? {type(d)}')
print(f'É do Alfabeto? {d.isalpha()}')
print(f'É Alfanumerico? {d.isalnum()}')
print(f'É minusculo? {d.islower()}')
print(f'É numerico? {d.isnumeric()}')
print(f'É maiusculo? {d.isupper()}')