#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,mostre a média entre todos os valores e qual foi
# o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valor
resp = 'S'
soma = media = cont = maior = menor = 0
while resp in 'Ss':
    numero = int(input('Digite um número: '))
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números, a soma foi {} e a média foi {}'.format(cont, soma, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))






