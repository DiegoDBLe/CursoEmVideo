# FAÇA UM PROGRAMA QUE LEIA O NOME E A MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO. NO FINAL, MOSTRE O CONTEUDO DA ESTRUTURA NA TELA
dicionario = {}
for c in range(1):
    dicionario['Nome: '] = str(input('Nome: ').upper().strip())
    dicionario['Média: '] = float(input(f'Média de {dicionario["Nome: "]}: '))
    if dicionario['Média: '] >= 7:
        print(f'Nome é igual a {dicionario["Nome: "]}\nMédia é igual a {dicionario["Média: "]}\nSituação é igual a Aprovado!')
    else:
        print(f'Nome é igual a {dicionario["Nome: "]}\nMédia é igual a {dicionario["Média: "]}\nSituação é igual a Reprovado!')
# SOLUÇÃO PROFESSOR:
aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().upper()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação!'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
