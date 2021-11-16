#REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO: EQUILATERO: TODOS OS LADOS IGUAIS,
# ISÓSCELES: DOIS LADOS IGUAIS, ESCALENO: TODOS OS LADOS DIFERENTES.
print('-=-' * 20)
print('ANALISADOR DE TRIANGULO')
print('-=-' * 20)
r1 = float(input('Digite o Primeiro Segmento: '))
r2 = float(input('Digite o Segundo Segmento:  '))
r3 = float(input('Digite o Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO!')
    if r1 == r2 and r2 == r3 and r3 == r1:
        print('Todos os Lados são iguais: Foi formado um Triângulo EQUILATERO!')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Todos os Lados Diferentes: Foi formando um Trinângulo ESCALENO!')
    else:
        print('Dois lados iguais: Foi formado um triangulo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO FORMA um triangulo!')

# ABAIXO SOLUÇÃO DO PROFESSOR:
print('-=-' * 20)
print('ANALISADOR DE TRIANGULO')
print('-=-' * 20)
r1 = float(input('Digite o Primeiro Segmento: '))
r2 = float(input('Digite o Segundo Segmento:  '))
r3 = float(input('Digite o Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO FORMA um triangulo!')
