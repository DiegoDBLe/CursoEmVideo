# CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA. NO FINAL MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM
# E PERMITA QUE O USÚARIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE:
from time import sleep
ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().upper()
    nota1 = float(input(f'Digite a 1° nota do(a) {nome}: '))
    nota2 = float(input(f'Digite a 2° nota do(a) {nome}: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] : ')).strip().upper()
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 26)
    opc = int(input('Selecione a opção referente ao aluno(a) que deseja ver a nota: (999 Interrompe o programa): '))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(2)
        print('<<VOLTE SEMPRE>>')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    if opc >= len(ficha):
        print('[OPÇÃO INVÁLIDA]')
        opc = int(input('Selecione a opção referente ao aluno(a) que deseja ver a nota: (999 Interrompe o programa): '))
