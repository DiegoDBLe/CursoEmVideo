''' Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

numero = int(input('Digite um numero: '))
antecessor = numero - 1
sucessor = numero + 1
print(f'O Antecessor de {numero} é: {antecessor} e o sucessor é: {sucessor}')

# OU

print(f'O Antecessor de {numero} é: {numero - 1} e o Sucessore é: {numero + 1}')
