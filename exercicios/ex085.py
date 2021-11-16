# CRIE UM PROGRAMA ONDE O USÚARIO POSSA DIGITAR SETE VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTENHA SEPARADOS OS VALORES PARES E IMPARES.
# NO FINAL, MOSTRE OS VALORES PARES E IMPARES EM ORDEM CRESCENTE.
listaNumerica = [[], []]
numeros = 0
for c in range(1, 8):
    numero = int(input(f'Digite o {c}° valor: '))
    if numero % 2 == 0:
        listaNumerica[0].append(numero)
    else:
        listaNumerica[1].append(numero)
listaNumerica[0].sort()
listaNumerica[1].sort()
print('-=-' * 30)
print(f'Os valores pares: {listaNumerica[0]}')
print(f'Os valores impares: {listaNumerica[1]}')

