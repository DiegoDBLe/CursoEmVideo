# FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE
# CONQUISTOU NO FINAL DO JOGO.
from random import randint
venceu = 'VOCÊ VENCEU!'
perdeu = 'GAME OVER!'
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR: ')
print('-=' * 20)
tentativa = 0
while True:
    computador = randint(0, 10)
    print('-' * 40)
    # AQUI EU PODERIA SUBISTITUIR ABAIXO POR -> WHILE parImpar not in 'PI' POIS JA VALIDARIA O PAR OU IMPAR E DIMINUIRIA UM IF
    jogador = int(input('Digite um valor: '))
    parImpar = str(input('Par ou Impar ? [P/I]: ')).upper().strip()[0]
    print('*' * 40)
    total = jogador + computador
    resultado = ''
    if total % 2 == 0:
        resultado = 'DEU PAR!'
        if parImpar in 'Pp':
            print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi: {total} -> {resultado}')
            print('-' * 40)
            print(f'\033[1;32m{venceu}!\033[m \nVamos jogar novamente...')
            tentativa += 1
        if resultado == 'DEU IMPAR!' or parImpar in 'Ii':
            print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi: {total} -> {resultado}')
            print('-' * 40)
            print(f'\033[1;31m{perdeu}\033[m Você venceu {tentativa} vezes')
            break
    elif total % 2 == 1:
        resultado = 'DEU IMPAR!'
        if parImpar in 'Ii':
            print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi: {total} -> {resultado}')
            print('-' * 40)
            print(f'\033[1;32m{venceu}!\033[m \nVamos jogar novamente...')
            tentativa += 1
        elif resultado == 'DEU IMPAR!':
            print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi: {total} -> {resultado}')
            print('-' * 40)
            print(f'\033[1;31m{perdeu}\033[m Você venceu {tentativa} vezes')
            break
# SOLUÇÃO DO PROFESSOR ABAIXO:
# computador = randint(0, 11)
# total = jogador + computador
# tipo = ' '
# while tipo not in 'PI':
#   tipo = str(input('Par ou Impar ? [P/I]: ')).upper().strip()[0]
# print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi: {total}')
# print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR'
# if tipo == 'P':
#   if total % 2 == 0:
#       print('Você Venceu!')
#       vitória += 1
#   else:
#       print('Você Perdeu!')
#       break
#   elif tipo == 'I':
#       if total % 2 == 1 :
#           print('Você VENCEU!')
#           vitoria += 1
#       else:
#           print('Você Perdeu')
#           break
#       print('Vamos jogar novamente...')
# print(f'GAME OVER! Você venceu {vitoria} vezes.'}