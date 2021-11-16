# QUANDO VOCÊ SABE O LIMITE DO LOOP É MELHOR USAR O ''FOR'' QUANDO NÃO SABE O LIMITE USA-SE O ENQUANTO( WHILE)
# ESTRUTURA DE REPETIÇÃO WHILE
from time import sleep

print('Estrutura For:')
for c in range(1, 11):
    print(c)
print('FIM')
print('-=-' * 20)
print(' ')
print('Estrutura While: ')
cont = 1
while cont < 11:
    print(cont)
    cont += 1
print('FIM')
print('*=-*=' * 30)
print('While onde faz o laço até o usuario digitar um numero que pare o loop: ')
n = 1
while n != 0:
    n = int(input('Digite um numero:'))
print('FIM')
print('*=-*=' * 30)
print('Solicitando a resposta do usuario e dependendo do que ele escolher encerra o loop: ')
r = 'S'
while r == 'S':
    n = int(input('Digite um numero:'))
    r = str(input('Quer continuar? : [S/N]')).upper()
print('Encerrando...')
sleep(2)
print('FIM')
print('*=-*=' * 30)
print('Solicitando a resposta do usuario e dependendo do que ele escolher encerra o loop e saber quantos números são pares e quantos são impares: ')
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você Digitou: \033[1;32m{} números pares\033[m e \033[1;33m{} números impares\033[m.'.format(par, impar))
