# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUARIO SE ELAS PODEM OU NÃO FORMAR UM TRIANGULO
# Cada segmento tem que ser menor que a soma dos outros dois segmentos
print('-=-' * 20)
print('ANALISADOR DE TRIANGULO')
print('-=-' * 20)
r1 = float(input('Digite o Primeiro Segmento: '))
r2 = float(input('Digite o Segundo Segmento:  '))
r3 = float(input('Digite o Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO!')
else:
    print('Os segmentos acima NÃO FORMA um triangulo!')
