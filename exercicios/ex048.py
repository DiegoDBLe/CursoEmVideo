# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA APENAS DOS QUE FOREM PARES. SE O VALOR DIGITADO FOR IMPAR DESCONSIDERE-O:
s = 0
cont = 0
for c in range(1, 6 + 1):
    n1 = int(input('Digite o {}° numero: '.format(c)))
    if n1 % 2 == 0:
        s += n1
        cont += 1
print('Somando todos os {} numeros pares, total: {}'.format(cont, s))
