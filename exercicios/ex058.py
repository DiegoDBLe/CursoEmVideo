# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SE FATORIAL
# 1° OPÇÃO UTILIZANDO A BIBLIOTECA DE MATEMÁTICA
from math import factorial
numero = int(input('Digite um número para calcular seu fatorial !: '))
fatorial = factorial(numero)
print('O Fatorial de {}! é {}'.format(numero, fatorial))

print('=' * 20)

# 2° OPÇÃO FAZENDO DA FORMA TRADICIONAL:
numero1 = int(input('Digite um número para calcular seu Fatorial !: '))
c = numero1
f = 1
print('Calculando {}! = '.format(numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

print('=' * 20)

# 3° OPÇÃO USANDO O FOR:
numero2 = int(input('Digite um número para calcular seu Fatorial !: '))
f = 1
for c in range(1, numero2+1):
    f *= c
print('O Fatorial de {}! é {}'.format(numero2, f))

