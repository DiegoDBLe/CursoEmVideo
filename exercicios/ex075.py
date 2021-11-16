# DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE A) QUANTAS VEZES APARECEU O VALOR 9;
# B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3; C) QUAIS FORAM OS NÚMEROS PARES
numero = (int(input('Digite um número: ')),
          int(input('Digite mais número: ')),
          int(input('Digite outro numero: ')),
          int(input('Digite o útimo número: ')))
print(f'Você digitou os números: {numero}')
print(f'Você digitou o 9 : {numero.count(9)} vezes')
if 3 in numero:
    print(f'O primeiro número 3 foi digitado na {numero.index(3)+1}° posição')
else:
    print('Não foi digitado o número 3')
print(f'Os números pares foram: ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')

