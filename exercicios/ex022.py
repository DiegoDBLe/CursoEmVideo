#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME 'SANTO':
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('O nome da cidade possui a palavra SANTO?:', cidade[:5].upper() == 'SANTO')
