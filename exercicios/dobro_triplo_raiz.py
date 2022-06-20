''' Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

numero = int(input('Digite um numero: '))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)# ou pow()

print(f'O Dobro de {numero} é: {dobro}\nO Triplo é: {triplo}\nA Raiz Quadrada é: {raiz_quadrada:.2f}')

# OU
print()
print(f'O Dobro de {numero} é: {numero * 2}\nO Triplo é: {numero * 3}\nA Raiz Quadrada é: {numero ** (1/2):.2f}')

print()
print(f'A Raiz Quadrada é: {pow(numero,(1/2)):.2f}')