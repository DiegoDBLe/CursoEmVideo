# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOA. NO FINAL MOSTRE, QUAL FOI O MAIOR E O MENOR PESO LIDOS:

pesoMaior = 0
pesoMenor = 0
for c in range(0+1, 5+1):
    peso = float(input('Digite o peso do {}°: '.format(c)))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print('O maior peso lido foi de {}Kg'.format(pesoMaior))
print('O menor peso lido foi de {}Kg'.format(pesoMenor))
