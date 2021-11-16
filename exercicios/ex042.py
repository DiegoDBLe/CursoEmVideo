#ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# À VISTA DINHEIRO / CHEQUE: 10% DE DESCONTO,  À VISTA NO CARTÃO: 5% DE DESCONTO, 2X OU MAIS NO CARTÃO 20% DE JUROS
print('-=' * 30)
print('-' * 10, 'FORMAS DE PAGAMENTO:', '-' * 10)
print('-Digite 1: PAGAMENTO À VISTA \n-Digite 2: PAGAMENTO À VISTA CARTÃO DE CREDITO \n-Digite 3: PAGAMENTO PARCELADO NO CARTÃO DE CREDITO')
print('-=' * 30)
preco = float(input('Qual o preço do Produto R$ '))
formaPagamento = int(input('Digite a forma de pagamento: '))
aVista = preco - (preco * 10 / 100)
aVistaCartao = preco - (preco * 5 / 100)
cartaoParcelado = preco + (preco * 20 / 100)
if formaPagamento == 1:
    print('Produto custa R$ {:.2f} reais com desconto de 10% valor total fica R$ \033[1;32m{:.2f}\033[m reais'.format(preco, aVista))
elif formaPagamento == 2:
    print('Produto custa R$ {:.2f} reais com desconto de 5% valor total fica R$ \033[1;32m{:.2f}\033[m reais'.format(preco, aVistaCartao))
elif formaPagamento == 3:
    quantidade = int(input('Deseja parcelar em quantas vezes: '))
    valorParcela = cartaoParcelado / quantidade
    print('Produto custa R$ {:.2f} reais \033[1;31mparcelando em {} x será cobrado juros de 20%\033[m valor total R$ {:.2f} reais'
          ' \n ficando: \033[1;31m{}x de R$ {:.2f}\033[m'
          .format(preco, quantidade, cartaoParcelado, quantidade, valorParcela))
else:
    print('\033[1;31m[ERROR]  OPÇÃO INVÁLIDA, ESCOLHA UMA OPÇÃO DE PAGAMENTO VÁLIDA.\033[m')
