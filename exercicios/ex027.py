#FAÇA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO. A MULTA VAI CUSTAR
# R$ 7,00 POR CADA KM ACIMA DO LIMITE
velocidade = float(input('Digite quantos Km/h o veiculos estava? : '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi MULTADO!! Pois estava acima do permitido de 80Km/h e vai pagar uma multa de R$ {:.2f} reais'.format(multa))
else:
    print('Bom dia! Velocidade dentro do limite de 80km/h Dirija com segurança')

