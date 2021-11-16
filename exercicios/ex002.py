n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero:'))

soma = n1 + n2

#print('A soma entre ', n1, 'e', n2, ' é ', soma)

print('A soma entre {} e {} vale: {}{}'.format(n1, n2, '\033[1;31m', soma))
