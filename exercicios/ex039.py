# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE
# ATÉ 9 ANO (MIRIM), ATÉ 14 ANOS(INFATIL), ATÉ 19 ANOS (JUNIOR), ATÉ 25 ANOS (SÊNIOR) E ACIMA (MASTER)
from datetime import date
nome = str(input('Digite seu nome: '))
anoNascimento = int(input('Sr(a).{} Digite o ano do seu nascimento: '.format(nome)))

idade = date.today().year - anoNascimento
if idade >= 0 and idade <= 9:
    print('Sua idade é \033[1;32m{}\033[m anos e você se qualifica na categoria: \033[1;32mMIRIM\033[m'.format(idade))
elif idade > 9 and idade <= 14:
    print('Sua idade é \033[1;32m{}\033[m anos e você se qualifica na categoria: \033[1;32mINFATIL\033[m'.format(idade))
elif idade > 14 and idade <= 19:
    print('Sua idade é \033[1;32m{}\033[m anos e você se qualifica na categoria: \033[1;32mJUNIOR\033[m'.format(idade))
elif idade > 19 and idade <= 25:
    print('Sua idade é \033[1;32m{}\033[m anos e você se qualifica na categoria: \033[1;32mSÊNIOR\033[m'.format(idade))
elif idade < 0 or idade >= 120:
    print('\033[1;31m[ERROR] DIGITE UM ANO VÁLIDO!!\033[m')
else:
    print('Sua idade é \033[1;32m{}\033[m anos e você se qualifica na categoria: \033[1;32mMASTER\033[m'.format(idade))
