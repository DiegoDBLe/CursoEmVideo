# CRIE UM PROGRAMA QUE LEIA VÁRIOS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS
# NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES, DESCONSIDERANDO O FLAG
s = c = 0
while True:
    numero = int(input('Digite um número: (999 para parar) '))
    if numero == 999:
        break
    c += 1
    s += numero
print(f'Foram digitados {c} numeros e a soma foi {s}')
