# CRIE UM PROGRAMA QUE LEIA: NOME, ANO DE NASCIMENTO, CARTEIRA DE TRABALHO E CADASTRE-OS (COM IDADE) EM UM DICIONÁRIO.
# SE POR ACASO A CTPS(CARTEIRA DE TRABALHO E PREVIDENCIA SOCIAL) FOR DIFERENTE DE ZERO, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DA CONTRATAÇÃO, E O SALÁRIO.
# CALCULE E ACRESCENTE, ALÉM DA IDADE COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.
from datetime import date
dicionario = {}

dicionario['Nome:'] = str(input('Nome: ')).strip().upper()
dicionario['idade:'] = int(input('Ano de Nascimento:'))
dicionario['idade:'] = date.today().year - dicionario["idade:"]
dicionario['CTPS:'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionario['CTPS:'] != 0:
    dicionario['Contratação:'] = int(input('Ano de Contratação: '))
    dicionario['Salário: R$ '] = float(input('Salário: R$ '))
    dicionario['Aposentadoria:'] = (dicionario["Contratação:"] - date.today().year) + 35 + dicionario["idade:"]
print('-=' * 30)
print(dicionario)
for x, y in dicionario.items():
    print(f'{x} {y}')

