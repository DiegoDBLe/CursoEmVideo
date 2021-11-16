# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO(NÚMERO INTEIRO) E O PROGRAMA
# VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES. OBS: CONSIDERE QUE O CAIXA SÓ POSSUI CEDULAS DE R$ 50,00 R$ 20,00 R$ 10,00 E R$ 1,00
from time import sleep
print('=' * 30)
print(' ' * 9, 'BANCO LBDB')  #ou print('{:^30}'.format('Banco LBDB'))
print('=' * 30)
saldo = 5000
novoSaldo = 0
print(f'Saldo: R$ {saldo}')
print('=' * 30)
saque = int(input('Que valor você quer sacar ? R$ '))
print('=' * 30)
while saque > saldo:
    saque = int(input('\033[1;31mSALDO INSUFICIENTE!\033[m\nQue valor você quer sacar ? R$ '))
print('{:^30}'.format('MENU'))
opcao = int(input(
    'OPÇÕES DE NOTA:\n[1] Notas de R$ 200,00 \n[2] Notas de R$ 100,00 \n[3] Notas de R$ 50,00 \n[4] Notas de R$ 20,00 '
    '\n[5] Notas de R$ 10,00 \n[6] Notas de R$ 5,00 \n[7] Notas de R$ 1,00 \nEscolha uma Opção: '))
print('=' * 30)
total = saque
#CÉDULAS:
cedulaDuzentos = 200
cedulaCem = 100
cedulaCinquenta = 50
cedulaVinte = 20
cedulaDez = 10
cedulaCinco = 5
cedulaUm = 1
#CONTADOR DE CÉDULAS
totalCedulaDuzentos = 0
totalCedulacem = 0
totalCinquenta = 0
totalVinte = 0
totalDez = 0
totalCinco = 0
totalUm = 0
while True:
    if opcao == 1 and total >= cedulaDuzentos:
        total -= cedulaDuzentos
        totalCedulaDuzentos += 1
    if total >= cedulaCem:
        total -= cedulaCem
        totalCedulacem += 1
    if total >= cedulaCinquenta:
        total -= cedulaCinquenta
        totalCinquenta += 1
    if total >= cedulaVinte:
        total -= cedulaVinte
        totalVinte += 1
    if total >= cedulaDez:
        total -= cedulaDez
        totalDez += 1
    if total >= cedulaCinco:
        total -= cedulaCinco
        totalCinco += 1
    if total >= cedulaUm:
        total -= cedulaUm
        totalUm += 1
    # QUANDO USUARIO NÃO QUISER SACAR NOTA DE R$ 200,00
    if opcao == 2 and total >= cedulaCem:
        total -= cedulaCem
        totalCedulacem += 1
    if total >= cedulaCinquenta:
        total -= cedulaCinquenta
        totalCinquenta += 1
    if total >= cedulaVinte:
        total -= cedulaVinte
        totalVinte += 1
    if total >= cedulaDez:
        total -= cedulaDez
        totalDez += 1
    if total >= cedulaCinco:
        total -= cedulaCinco
        totalCinco += 1
    if total >= cedulaUm:
        total -= cedulaUm
        totalUm += 1
    else:
        break
print(
    f'-> cedula200: R${cedulaDuzentos} -> total de cedula200: {totalCedulaDuzentos}'
    f'\n-> Cédula100: R$ {cedulaCem} -> total de cedulaCem: {totalCedulacem}'
    f'\n-> Cédula50: R$ {cedulaCinquenta} -> total de cedulaCinquenta: {totalCinquenta}'
    f'\n-> Cédula20: R$ {cedulaVinte} -> total de cedulaVinte: {totalVinte}'
    f'\n-> Cédula10: R$ {cedulaDez} -> total de cedulaDez: {totalDez}'
    f'\n-> Cédula5: R$ {cedulaCinco} -> total de cedulaCinco: {totalCinco}'
    f'\n-> Cédula1: R$ {cedulaUm} -> total de cedulaUm: {totalUm}')
sleep(2)
print('Contando Notas......')
sleep(5)
print('Saque Reslizado com Sucesso!')
novoSaldo = saldo - saque
print('=' * 30)
print(f'Saldo Atual: R$ {novoSaldo:.2f}')
print('Volte sempre ao BANCO LBDB! Tenha um Bom Dia!')
