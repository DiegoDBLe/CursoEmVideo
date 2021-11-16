# CRIE UM PROGRAMA QUE LEIA NOME, SEXO, E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA.
# NO FINAL, MOSTRE: A) QUANTAS PESSOAS FORAM CADASTRADAS; B) A MÉDIA DE IDADE DO GRUPO; C) UMA LISTA COM TODAS AS MULHERES; D) UMA LISTA COM TODOAS AS PESSOAS COM IDADE ACIMA DA MÉDIA.
dicionario = {}
lista = []
cont = media = somaIdade = 0
while True:
    cont += 1
    dicionario['Nome'] = str(input('Nome: ')).strip().upper()
    while True:
        dicionario['Sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if dicionario['Sexo'] in 'MF':
            break
        print('\033[1;31m[ERROR]\033[m Por favor, digite apenas M ou F. ')
    dicionario['Idade'] = int(input('Idade: '))
    somaIdade += dicionario['Idade']
    lista.append(dicionario.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('\033[1;31m[ERROR]\033[m Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
dicionario = lista
print('-=' * 30)
print(f'- O grupo tem {cont} pessoas.')
media = somaIdade / cont
print(f'- A média de idade é {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in lista:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}, ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in dicionario:
    if p['Idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
print(dicionario)
