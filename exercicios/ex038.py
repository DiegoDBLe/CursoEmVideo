#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:
nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota:  '))
media = (nota1 + nota2) / 2
print('tirando {} e {}: '.format(nota1, nota2))
if media <= 5.0:
    print('Sua média foi: {:.2f}\033[1;31m: ALUNO REPROVADO\033[m'.format(media))
elif media >= 5.1 and media <= 6.9:
    print('Sua média foi: {:.2f}\033[1;33m: ALUNO EM RECUPERAÇÃO\033[m'.format(media))
elif media >= 7.0 and media <= 10:
    print('Sua média foi: {:.2f} \033[1;32m: ALUNO APROVADO!\033[m'.format(media))
elif media >= 11:
    print('\033[1;31m[ERROR] ESSA NOTA {} É INEXISTENTE:\033[m'.format(media))
