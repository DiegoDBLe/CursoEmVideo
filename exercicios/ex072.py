# CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSÃO, DE ZERO ATÉ VINTE. SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO
# ENTRE 0 E 20 E MOSTRA-LO POR EXTENSO.
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'terze', 'quartoze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resposta = ''
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número: {extenso[numero]}')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resposta in 'Nn':
            print('Obrigado!! Até a próxima')
            break