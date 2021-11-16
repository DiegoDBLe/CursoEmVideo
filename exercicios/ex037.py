# ESCREVA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
# SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA DE SE ALISTAR OU SE JÁ PASSOU DO TEMPO DO ALISTAMENTO. TAMBÉM DEVERA MOSTRAR O TEMPO QUE FALTA PRA SE ALISTAR
from datetime import date
nome = str(input('Digite seu nome: '))
anoNascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - anoNascimento
falta = 18 - idade
if idade >= 17 and idade < 18:
    print('Você {}, tem \033[1;32m{}\033[m anos. Procure uma base do exército mais próxima para seu Alistamento Militar.'.format(nome, idade))
elif idade >= 18 and idade <= 21:
    print('Você {}, tem \033[1;32m{}\033[m anos. Procure uma base do exército mais próxima \033[1;31mURGENTE!\033[m. para seu Aistamento Militar.'.format(nome, idade))
elif idade < 17:
    print('Você {}, tem \033[1;32m{}\033[m anos. Falta {} anos para seu Alistamento Militar.'.format(nome, idade, falta))
else:
    print('Você {}, Já passou da idade de Alistamento Militar.'.format(nome))

# SOLUÇÃO DO PROFESSOR ABAIXO:

atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
