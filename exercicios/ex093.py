# CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU.
# DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO
dicionario = {}
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
print(dicionario)
print('-=' * 30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O Jogador {dicionario["Nome do jogador"]} jogou {partidas} partidas.')
for i, v in enumerate(dicionario['Gols']):
     print(f'   => Na {i+1}° partida , fez {v} gols.')
print(f'Foi um total de {dicionario["Total Gols"]} gols.')




