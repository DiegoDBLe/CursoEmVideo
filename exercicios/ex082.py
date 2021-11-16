# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA: DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES E OS IMPARES
# DIGITADOS, RESPECTIVAMENTE. AO FINAL, MOSTRE O CONTEUDO DAS TRêS LISTAS GERADAS.
lista = list()
listaPares = list()
listaImpares = list()
while True:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)
    resposta = str(input('Quer Continuar? [S/N] ')).strip().upper()
    if resposta in 'Nn':
        break
lista = listaImpares + listaPares
lista.sort()
print(f'Lista Completa: {lista}')
print(f'Lista Pares: {listaPares}')
print(f'Lista Impar: {listaImpares}')
print('-=-' * 30)
print()

# SOLUÇÃO DO PROFESSOR:
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=-' * 30)
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')