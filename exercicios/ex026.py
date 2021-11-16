#FAÇA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NUMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO ESCOLHIDO PELO
# COMPUTADOR. O PROGRAMA DEVERA ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU
import random
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
acertou = random.choice(lista)
numero = int(input('Entre 0 e 5: Qual numero estou pensando? : '))
print('Eu pensei no: {}'.format(acertou))
if numero == acertou:
    print('Parabéns!! Você GANHOU')
else:
    print('Tente Novamente! Você PERDEU')

# OU ABAIXO ESTA A SOLUÇÃO DO PROFESSOR:
computador = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
