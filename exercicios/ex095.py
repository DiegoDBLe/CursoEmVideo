# APRIMORE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR.
from time import sleep
time = []
dicionario = {}
while True:
    dicionario.clear()
    dicionario['Nome do jogador'] = str(input('Nome do jogador: ')).strip().upper()
    partidas = int(input(f'Quantas partidas {dicionario["Nome do jogador"]} jogou: '))
    gols = []
    totGols = 0
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na {p+1}° partida ? : ')))
    dicionario['Gols'] = gols
    # Assim:
    # for s in gols:
    #     totGols += s
    # ou assim:
    dicionario['Total Gols'] = sum(gols)
    print('-=' * 30)
    time.append(dicionario.copy())
    while True:
        resp = str(input('Quer continuar? {S/N} ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('\033[1;31m[ERROR]\033[m Responda apenas com S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod. ', end='')
for i in dicionario.keys():
    print(f' {i:<15} ', end='')
print()
for k, v in enumerate(time):
    print(f' {k:>3} ', end='')
    for d in v.values():
        print(f' {str(d):<15} ', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar dados de qual jogador? \033[1;31m[999 para encerrar a busca]\033[m: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'\033[1;31m[ERROR]\033[m Não existe jogador com código {busca}!')
    else:
        print(f' ---- LEVATAMENTO DO JOGADOR {time[busca]["Nome do jogador"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('FINALIZANDO...')
sleep(2)
print('\033[1:32m<< VOLTE SEMPRE >>\033[m')

