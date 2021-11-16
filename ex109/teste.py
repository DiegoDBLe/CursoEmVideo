from ex109 import moeda
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem parametros a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108.

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10% do preço temos: {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 10% do preço temos: {moeda.diminuir(preco, 10, True)}')
