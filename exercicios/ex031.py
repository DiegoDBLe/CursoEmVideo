#FAÇA UM PROGRAMA QUE LEIA TRÊS NUMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))
lista = {numero1, numero2, numero3}
print('O maior numero é {}'.format(max(lista)))
print('O menor numero é {}'.format(min(lista)))
