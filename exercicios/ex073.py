# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
# A) APENAS OS 5 PRIMEIROS; B) OS ULTIMOS 4 COLOCADOS DA TABELA; C) UMA LISTA COM OS TIMES EM ORDEM ALFABETICA; D) EM QUAL POSIÇÃO ESTÁ O TIME CHAPECOENSE.
times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atlético-GO', 'Ceará SC', 'Internacional', 'Santos', 'São Paulo',
         'Fluminense', 'Juventude', 'Cuiabá', 'Bahia', 'Grêmio', 'América-MG', 'Sport-Recife', 'Chapecoense')

for c in range(0, 5, len(times)):
    print(f'-> Classificação para Libertadores:  {times[c:5]}')

    print(f'-> Rebaixados Para serie B: {times[15:]}')

    print('-> Ordem Alfabética: ', sorted(times))
    print('-> Qual posição está o time da Chapecoense? \nNa posição: ', times.index('Chapecoense')+1)
print('*' * 100)
# SOLUÇÃO PROFESSOR ABAIXO:
print('-=-' * 30)
print('{:^90}'.format('BRASILEIRÃO'))
print('-=-' * 30)
for t in times:
    print(f'{t}')
print('-=-' * 30)
print(f'Lista dos times: {times}')
print('-=-' * 30)
print(f'Os 5 primeiros times: {times[0:5]} ')
print('-=-' * 30)
print(f'Os 4 ultimos times são: {times[-4:]}')
print('-=-' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-' * 30)
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}° posição ')

