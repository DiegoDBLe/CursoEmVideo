# REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o Primeiro Termo:  '))
razao = int(input('Digite a Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(' {} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
