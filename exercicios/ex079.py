# Crie um programa onde o usuario possa digitar vários valores númericos e cadastrar todos em uma lista.
# Caso o numero já exista la dentro, ele não será adicionado. No final serão exibidos valores únicos digitados em ordem crescente
lista = list()
while True:
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!! Não vou adicionar...')
    continuar = str(input('Quer Continuar? [S/N]')).strip().upper()
    if continuar in 'Nn':
        print('=-=' * 50)
        lista.sort()
        print(f'Você digitou os valores: {lista}')
        break
