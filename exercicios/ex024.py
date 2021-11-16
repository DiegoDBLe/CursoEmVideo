#CRIE UM PROGRAMA QUE LEIA UMA FRASE E PELO TECLADO MOSTRE:
# - QUANTAS VEZES APARECE A LETRA 'A'
# - EM QUAL POSIÇÃO ELA APARECE A PRIMEIRA VEZ
# - EM QUAL POSIÇÃO ELA APARECE A ULTIMA VEZ

frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra "a ou A": {} '.format(frase.count('A')))
print('Primeira vez na posição: {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
