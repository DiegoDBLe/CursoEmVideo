# MELHORE O DESAFIO 028(026) ONDE O COMPUTADOR VAI PENSAR EM UM NÚMERO ENTRE 0 E 10 VAI TENTAR ADIVINHA ATÉ ACERTAR,
# MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER.
import random
from time import sleep

computador = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei? '))
print('PROCESSANDO...')
sleep(1)
cont = 0
while computador != jogador:
    jogador = int(
        input('\033[1;31mERROU\033[m tente novamente: \n Em que numero estou pensando? : '.format(computador)))
    cont += 1
    if jogador == computador:
        print('\033[1;32mPARABENS!\033[m Você conseguiu me vencer na {}° tentativa.'.format(cont))
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print('Realmente eu pensei no número \033[1;32m{}\033[m'.format(computador))
