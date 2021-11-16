#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
# 1 - PARA BINÁRIO        2 - PARA OCTAL      3 - HEXADECIMAL
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAl
[ 3 ] HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[1;31m[ERROR] OPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
