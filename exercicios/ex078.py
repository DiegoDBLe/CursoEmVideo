# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA. NO FINAL, MOSTRE O MAIOR E O MENOR VALOR DIGITADO E SUAS RESPECTIVAS POSIÇÕES NA LISTA
lista = []
for c in range(1, 5+1):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição: ')
print(f'O menor valor digitado foi {min(lista)} na posição: ')
# NESSA MIMHA SOLUÇÃO SÓ CONSIGO TER O MAIOR E O MENOR NÚMERO, POIS PARA MOSTRAR A POSIÇÃO TENHO Q TER A VARIAVEL MAIOR E MENOR.
# ABAIXO SOLUÇÃO DO PROFESSOR:
print()
print()
print('-=-' * 30)
listaNum = []
maior = menor = 0
for c in range(0, 5):
    listaNum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = listaNum[c]
    else:
        if listaNum[c] > maior:
            maior = listaNum[c]
        if listaNum[c] < menor:
            menor = listaNum[c]
print('-=-' * 30)
print(f'Você digitou os valores: {listaNum}')
print(f'O maior valor digitado foi: {maior} nas posições ', end='')
for i, v in enumerate(listaNum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi: {menor} nas posições ', end='')
for i, v in enumerate(listaNum):
    if v == menor:
        print(f'{i}...', end='')
