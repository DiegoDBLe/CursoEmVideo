# SEM FORMATAÇÃO
a = input('Digite Algo:')
print('Qual o tipo primitivo? ', type(a))
print('Só Tem espaço? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É Alfabético? ', a.isalpha())
print('É Alfanumerico? ', a.isalnum())
print('Está em MAIUSCULO? ', a.isupper())
print('Esta em minusculo? ', a.islower())
print('Palavra está captalizada? ', a.istitle())

#COM FORMATAÇÃO
b = input('Digite Algo:')
print('Qual o tipo primitivo? {}'.format(type(a)))
print('Só tem espaço? {}'.format(b.isspace()))
print('É um numero? {}'.format(b.isnumeric()))
print('É alfabetico? {}'.format(b.isalpha()))
print('É Alfanumerico? {}'.format(b.isalnum()))
print('Está MAIUSCULO? {}'.format(b.isupper()))
print('Está miusculo? {}'.format(b.islower()))
print(('Palavra está captalizada? {}'.format(b.istitle())))

# OBS: Não tem difereça nenhuma nesse exercicio