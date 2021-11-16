# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS DE CADA VEZ , PARA CADA VALOR QUE O USUÁRIOS DIGITAR. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO
# FOR NEGATIVO:
c = 0
while True:
    numero = int(input('Quer ver a tabuada de qual valor : '))
    print('-' * 30)
    if numero < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    for c in range(1, 10+1):
        print(f'{numero} x {c} = {numero * c}')
    print('-' * 30)
