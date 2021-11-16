# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO(NÚMERO INTEIRO) E O PROGRAMA
# VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES. OBS: CONSIDERE QUE O CAIXA SÓ POSSUI CEDULAS DE R$ 50,00 R$ 20,00 R$ 10,00 E R$ 1,00
print('=' * 30)
print('{:^30}'.format('Banco LBDB'))
print('=' * 30)
saque = int(input('Qual o valor a ser sacado: R$ '))
total = saque
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:          # Aqui pega o valor total que é o valor do saque se ele for maior que o valor da cedula, o valor total vai diminuir o valor da cedula no valor total. ex: 100 - 50 e assim ate o  total zerar ou ser menor que o valor da cedula
        total -= cedula          # Aqui vai decrementar o valor da cédula do valor total
        totalCedula += 1         # Aqui vai contar quantas notas de 50 foi preciso para chegar ao valor total
    else:                        # Se o valor total for menor que o da cedula, vai entrar no else
        if totalCedula > 0:      # Aqui é pra não mostrar o contador de nota que for 0, somente os acima de zero
            print(f'Total de {totalCedula} cédulas de R$ {cedula:.2f}')
        if cedula == 50:        # Se a cedula for igual a 50 ou menor
            cedula = 20         # cédula vai receber o valor de 20 que é a próxma nota abaixo de 50
        elif cedula == 20:      # senao a cédula for igual a 20 ou menor
            cedula = 10         # vai receber o valor da próxima nota abaixo de 20 que é 10
        elif cedula == 10:      # senao a cédula for igual a 10 ou menor
            cedula = 5          # cédula vai receber a nota abaixo de 10 que é 5
        elif cedula == 5:       # senao a cédula for igual ou menor que 5
            cedula = 1          # cédula vai receber a nota abaixo de 5 que é 1
        totalCedula = 0         # Aqui é zerado pois toda vez que passar por aqui o laço vai zerar quantidade de determinada nota
        if total == 0:          # quando o total for igual a 0 ou seja nao tiver mais dinheiro comando break entra em ação
            break
print('=' * 30)
print('Volte sempre ao BANCO LBDB! Tenha um Bom Dia!')