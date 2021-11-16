#OPERADORES ARITIMETICOS E FORMATAÇAO DO PRINT
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}:  \nSubtração {}: \nMultiplicação {}: \nDivisão {:.3f}:'.format(s, sub, m, d))
print('Divisão inteira {}: \nPortência {}:'.format(di, e))
