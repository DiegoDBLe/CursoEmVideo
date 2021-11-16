#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA:

aluno = input('Digite Seu nome: ')
n1 = float(input('Digite a primeira nota: '))
if n1 > 10:
    n1 = float(input('[ERROR]. Digite uma nota válida: '))
n2 = float(input('Digite a segunda nota: '))
if n2 >10:
    n2 = float(input('[ERROR]. Digite uma nota válida: '))
soma = n1 + n2
media = soma /2

if media <= 10:
    print('A Média do aluno: {} é {}'.format(aluno, media))
else:
    print('[ERROR]. Alguma nota foi digitada inválida:')
