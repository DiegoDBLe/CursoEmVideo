#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALIDROMO, DESCONSIDERANDO OS ESPAÇOS
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #Separei em uma coleção, para saber como fica é so printar palavras
junto = ''.join(palavras) #Juntando todas as palavras, para saber como fica é só printar a palavra junto
inverso = ''
for letra in range(len(junto) -1, -1, -1): # Vai varrer, len é para saber o tamanho da palavra digitada em junto, -1 pq vai começar da ultima letra, ate 0 porém -1, e vai andar uma casa pra tras por isso o outro -1
    inverso += junto[letra]
if inverso == junto:
    print('\033[1;31m{}\033[m é um PALINDROMO!'.format(frase))
else:
    print('\033[1;33m{} \033[m não é um Palindromo!'.format(frase))

#OU usando o Fatiamento:
''' No logar do for colocar a variavel inverso = junto[::-1] '''

