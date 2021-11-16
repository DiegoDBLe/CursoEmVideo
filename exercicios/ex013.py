#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDO POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO.
#CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO

km = float(input('Qual a KM percorrida com o carro: KM '))
dias = int(input('Quantos dias o carro foi alugado? '))

totalAPagar = (km * 0.15) + (dias * 60)

print('Total a Pagar é de R$ {:.2f}'.format(totalAPagar))
