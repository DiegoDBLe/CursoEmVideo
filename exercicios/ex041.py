#DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
# ABAIXO DE 18.5(ABAIXO DO PESO), ENTRE 18.5 E 25(PESO IDEAL), 25 ATÉ 30(SOBREPESO), 30 ATÉ 40(OBESIDADE), ACIMA DE 40(OBESIDADE MÓRBIDA)
nome = str(input('Digite seu nome: '))
peso = float(input('Sr(a).{} Digite seu peso Kg:  '.format(nome)))
altura = float(input('Sr(a).{} Digite sua altura : '.format(nome)))
imc = peso / (altura * altura) # ou (altura **2 )
if imc >= 0 and imc < 18.5:
    print('{} Seu IMC é {:.2f}, Você está muito ABAIXO DO PESO: \033[1;31mCUIDADO!!\033[m'.format(nome, imc))
elif imc >= 18.5 and imc < 25:
    print('{} Seu IMC é {:.2f}, Você está com PESO IDEAL: \033[1;32mPARABÉNS!!\033[m'.format(nome, imc))
elif imc >= 25 and imc < 30:
    print('{} Seu IMC é {:.2f}, Você está com SOBREPESO: \033[1;33mATENÇÃO!!\033[m'.format(nome, imc))
elif imc >= 30 and imc < 40:
    print('{} Seu IMC é {:.2f}, Você está com OBESIDADE: \033[1;31mCUIDADO!!\033[m'.format(nome, imc))
elif imc >= 40:
    print('{} Seu IMC é {:.2f}, Você está com OBESIDADE MÓRBIDA: \033[1;31mPROCURE UM MÉDICO URGENTE!!\033[m'.format(nome, imc))
