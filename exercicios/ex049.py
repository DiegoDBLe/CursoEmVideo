# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UM P.A. NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo, decimo + razao, razao):
    print('{} '.format(c), end=' -> ')
print('ACABOU')
    