#ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM C° PARA F°
celsius = float(input('Digite a temperatura em C° : '))
fahrennheit = ((9 * celsius) / 5) + 32
print('A temperatura de {} C° corresponde a {}F° !'.format(celsius, fahrennheit))
