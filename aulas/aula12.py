#ESTRUTURA DE REPETIÇÃO FOR
#print('\noi' * 10)
#CRESCENTE
# for c in range(0, 6,):
#     print('- {}'.format(c))
# print('FIM')
#
# #DECRESCENTE
# for c in range(6, 0, -1):
#     print('- {}'.format(c))
# print('FIM')
#
# #PULAR DE 2 EM 2
# for c in range(0, 7 , 2):
#     print('- {}'.format(c))
# print('FIM')
#
# #SOLICITANDO AO USUARIO ATÉ QUANTO QUER CONTAR
# n = int(input('Digite um numero: '))
# for c in range(0, n+1):
#     print(c)
# print('FIM')
#
# # SOLICITANDO AO USUARIO INICIO, FIM E PASSO
# inicio = int(input('Digite o Inicio: '))
# fim = int(input('Digite o Fim: '))
# passo = int(input('Digite o Passo:'))
# for c in range(inicio, fim+1, passo):
#     print('- {}'.format(c))
# print('FIM')
#
# # SOLICITAR AO USUARIO PARA DIGITAR ALGO REPETIDAS VEZES
# for c in range(0, 3):
#     n = int(input('Digite um numero: '))
# print('FIM')

# SOMANDO TODOS OS NUMEROS SOLICITADOS:
s = 0
for c in range(1, 4 +1):
    n = int(input('Ditige o {}° numero: '.format(c)))
    s += n
print('O somatório de todos os valore é {}'.format(s))
