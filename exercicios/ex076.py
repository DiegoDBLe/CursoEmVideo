# CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUENCIA.
# NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR:
print('-' * 40)
print('{:^35}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
for x in range(0, len(produtos)):
    if x % 2 == 0:
        print(f'{produtos[x]:.<30}', end='')
    else:
        print(f'R${produtos[x]:>7.2f}')
print('-' * 40)

print('-' * 40)
print('{:^40}'.format("LACHE DOGÃO"))
print('-' * 40)
lanches = ('Carne Moida', 10.45,
           'Misto', 10.00,
           'A Moda', 15.10,
           'Hot Dog', 9.75,
           'X-Calabresa', 12.10,
           'X-Tudo', 16.50)
for x in range(0, len(lanches)):
    if x % 2 == 0:
        print(f'{lanches[x]:.<30}', end='')
    else:
        print(f'R$ {lanches[x]:>7.2f}')









