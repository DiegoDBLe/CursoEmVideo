# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBE TRÊS PARAMETROS(INICIO, FIM E PASSO) E REALIZE A CONTAGEM.
# SEU PROGRAMA TEM QUE REALIZAR TRêS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
# A) DE 1 ATÉ 10, DE 1 EM 1     B) DE 10 ATÉ 0, DE 2 EM 2       C) CONTAGEM PERSONALIZADA.
from time import sleep


# def contador(i, m, p):
#     print('-=' * 30)
#     print(f'Contagem de {i} até {m} de {p} em {p}: ')
#     for n in range(1, 11, 1):
#         sleep(0.5)
#         print(f'{n} ', end='')
#     print('FIM!')
#     print('-=' * 30)
#     print('Contagem de 10 até 0 de 2 em 2: ')
#     for v in range(10, 0, -2):
#         sleep(0.5)
#         print(f'{v} ', end='')
#     print('FIM!')
#     print('-=' * 30)
#     print('Agora é a sua vez de personalizar a contagem!')
#     for x in range(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: '))):
#         sleep(0.5)
#         print(f' {x} ', end='')
#     print('FIM!')
def contador(inicio, fim, passo):

    if passo < 0: # Se o passo for menor que zero
        passo *= -1 # aqui transforma o passo em positivo.
    if passo == 0:
        print(f'[ERROR] o passo não pode ser {passo}. Quando digitado 0 recebe automaticamente o valor 1.')
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} contando de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
