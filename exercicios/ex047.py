#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER, SÓ QUE AGORA USANDO LAÇO FOR

#-TABUADA MULTIPLICAÇÃO
n1 = int(input('Digite um numero: '))
print('\033[1;31mN°{} Na MULTIPLICAÇÃO:\033[m'.format(n1))
for c in range(1, 10+1):
    tabuadaMultiplicacao = c * n1
    print('{:2} x {:2} = {:2}'.format(c, n1, tabuadaMultiplicacao))
    #OU
   # print('{:2} x {:2} = {:2}'.format(c, n1, n1*c))

#-TABUADA SUBTRAÇÃO
print('\n\033[1;31mN°{} Na SUBTRAÇÃO:\033[m'.format(n1))
if n1 == 1:
    for c in range(2, 11+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 2:
    for c in range(3, 12+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 3:
    for c in range(4, 13+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 4:
    for c in range(5, 14+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 5:
    for c in range(6, 15+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 6:
    for c in range(7, 16+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 7:
    for c in range(8, 17+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 8:
    for c in range(9, 18+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 9:
    for c in range(10, 19+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))
elif n1 == 10:
    for c in range(11, 20+1):
        tabuadaSubtracao = c - n1
        print('{:2} - {:2} = {:2}'.format(c, n1, tabuadaSubtracao))

# - TABUADA ADIÇÃO
print('\n\033[1;31mN°{} Na ADIÇÃO:\033[m'.format(n1))
for c in range(0, 10+1):
    tabuadAdicao = c + n1
    print('{:2} + {:2} = {:2}'.format(c, n1, tabuadAdicao))

# - TABUADA DIVISÃO
print('\n\033[1;31mN°{} Na DIVISÃO:\033[m'.format(n1))
for c in range(1, 10+1):
    tabuadaDivisao = n1 / c
    print('{:2} / {:2} = {:.2f}'.format(n1, c, tabuadaDivisao))

