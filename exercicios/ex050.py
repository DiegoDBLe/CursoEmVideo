#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO
n1 = int(input('Digite um numero: '))
tot = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        print(' \033[1;32m{}\033[m'.format(c), end=' ')
        tot += 1
    else:
        print(' {} '.format(c), end=" ")
print('\nO número {} foi divisivel {} vezes'.format(n1, tot))
if tot == 2:
    print('O número {} é PRIMO'.format(n1))
else:
    print('NÃO É PRIMO')
