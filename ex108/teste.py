from ex108 import moeda
# Adapte o código do exercicio 107 criando uma função adicional chamada moeda() que consiga mostrar os valores como um monetário formatado.
preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10% do preço temos: {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 10% do preço temos: {moeda.moeda(moeda.diminuir(preco, 10))}')
