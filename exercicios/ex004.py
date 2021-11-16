# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR:

n = int(input('Digite um numero: '))
print('Analisando o numero {}, seu antecessor é {} e seu sucessor é {}'.format(n, (n-1), (n+1)))
                                    # ou
# s = n + 1
# a = n - 1
# print('O Sucessor é: {}'.format(s))
# print('O Antecessor é: {}'.format(a))

# ou

print('Analisando o numero {}, seu antecessor é {} e seu sucessor é {}'.format(n, (n-1), (n+1)))

# CRIE UM ALGORITIMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA
dobro = n * 2
triplo = n * 3
raiz = n ** 2
print('O Dobro é:{}{:=}{}'.format('\033[1;31m', dobro, '\033[m'))
print('O Triplo é:{}{:=}{}'.format('\033[1;31m', triplo, '\033[m'))
print('A Raiz quadrada é: {}{:=}{}'.format('\033[1;31m', raiz, '\033[m'))
