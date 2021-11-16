# ESCREVA UM PROGRAMA PARA APROVAR UM EMPRESTIMO BANCARIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA,
# O SALARIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR. CALCULE O VALOR DA PRESTÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALARIO
# OU ENTAO O EMPRESTIMO SERÁ NEGADO.
nomeComprador = str(input('Qual o nome do Comprador: '))
valorCasa = float(input('Qual o valor do Imóvel? R$ '))
salarioComprador = float(input('Qual o salário do Sr(a).{} R$ '.format(nomeComprador)))
quantidadeParcela = int(input('Em quantos anos deseja pagar o Imovel? : '))
valorPrestacao = valorCasa / (quantidadeParcela * 12)
if valorPrestacao < salarioComprador * 30 / 100:
    print('Parabéns!! Sr(a).{}!! O Finaciamento do seu Imóvel foi \033[1;32mAPROVADO! \033[m'
           '\nSeu Financiamento ficou da seguinte forma: \033[1;32m{} x R$ {:.2f} reais\033[m'.format(nomeComprador, quantidadeParcela, valorPrestacao))
else:
    print('Sr(a). {} A parcela ficou R$ \033[1;31m{:.2f} reais. '
          '\nValor excedente de 30% do salário. \nEmpréstimo \033[1;31mNEGADO!'.format(nomeComprador, valorPrestacao))