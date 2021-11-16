lista1 = [3, 4, 1, 5, 1, 1]
lista2 = [2, 3, 4, 3, 2, 1]
lista3 = [0, 0, 0, 0, 0, 0]

for i in range(6):
    lista3[i] = lista1[i] + lista2[i]

print(lista3)
print(lista3[2])

T = 1
M = 5
C = 10

while T < M:
    C = C * (1 + T)
    T = T + 1

print(C)

from random import randint

n = 7
a = 0

for i in range(n):
    num_aleat = randint(0, 50)
    if num_aleat > a and num_aleat <= 40:
        a = num_aleat

print(a)


print('Bem-vindo(a)! Para abrir uma conta corrente responda às seguintes perguntas: ')

p1 = input('Você tem em mãos o documento de identidade, sim ou não?')
p2 = input('Você tem em mãos um comprovante de residência, sim ou não? ')

if p1 == 'não' or p2 == 'não':
    print('Sinto muito, você não tem os documentos necessários para a abertura de conta corrente.')
else:
    print('Certo. Vamos prosseguir com a abertura da sua conta corrente.')