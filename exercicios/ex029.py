# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS ATE 200KM E R$ 0,45 PARA VIAGENS MAIS LONGAS
distancia = float(input('Qual a distancia em KM da viagem? '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('O valor da passagem rodando {:.0f}Km é R$ {:.2f} reais'.format(distancia, passagem))
else:
    passagem = distancia * 0.45
    print('O valor da passagem rodando {:.0f}Km é R$ {:.2f} reais'.format(distancia, passagem))
