# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUARIO VAI CONTINUAR. NO FINAL MOSTRE:
# A) QUAL É O TOTAL GASTO NA COMPA; B) QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000; C) QUAL É O NOME DO PRODUTO MAIS BARATO;
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
total = maisDeMil = cont = maisBarato = 0
produto = ' '
while True:
    cont += 1
    nomerProduto = str(input('Nome do Produto: ')).strip()
    precoProduto = float(input('Preço: R$ '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    total += precoProduto
    if precoProduto > 1000:
        maisDeMil += 1
    if cont == 1 or precoProduto < maisBarato:
        maisBarato = precoProduto
        produto = nomerProduto
    if continuar in 'Nn':
        break
print(f'O Total da compra foi R$ {total :.2f}\nTemos {maisDeMil} produtos custando mais de R$ 1000,00'
          f'\nO Produto mais barato foi {produto} que custa R$ {maisBarato :.2f} ')

# SOLUÇÃO DO PROFESSOR:
# while True:
    # nomerProduto = str(input('Nome do Produto: ')).strip()
    # precoProduto = float(input('Preço: R$ '))
    # cont = 1
    # total += precoProduto
    # if precoProduto > 1000:
    #    maisDeMil += 1
    # if cont == 1 or precoProduto < maisBarato :
    #     maisBarato = precoProduto
    #     produto = nomerProduto
    # continuar = ' '
    #   while continuar not in 'SN':
    #        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    #   if continuar == 'N':
    #         break
# print(f'O Total da compra foi R$ {total :.2f}\nTemos {maisDeMil} produtos custando mais de R$ 1000,00'
#           f'\nO Produto mais barato foi {produto} que custa R$ {maisBarato :.2f} ')