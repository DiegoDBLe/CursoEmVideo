# FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIS PESSOAS, GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
# A) QUANTAS PESSOAS FORAM CADASTRADAS; B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS; UMA LISTAGEM COM AS PESSOAS MAIS LEVES;
listaPessoas = list()
listaDados = list()
pesado = leve = 0
while True:
    listaDados.append(str(input('Digite seu nome: ')).upper())
    listaDados.append(float(input(f'Seu peso Sr(a).{listaDados[0]} - Kg: ')))
    if len(listaPessoas) == 0:
        pesado = leve = listaDados[1]
    else:
        if listaDados[1] > pesado:
            pesado = listaDados[1]
        if listaDados[1] < leve:
            leve = listaDados[1]
    listaPessoas.append(listaDados[:])
    listaDados.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar in 'Nn':
        break
print('-=-' * 30)
print(f'Ao todo você cadastrou {len(listaPessoas)} pessoas. ')
print(f'O maior peso digitado foi de {pesado} Kgs.', end='')
for p in listaPessoas:
    if p[1] == pesado:
        print(f'{p[0]}')
print(f'O menor peso digitado foi de {leve} kgs.', end='')
for p in listaPessoas:
    if p[1] == leve:
        print(f'{p[0]}')
