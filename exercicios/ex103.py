# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU. O PROGRAMA DEVERÁ
# SE CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE.
def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols.')


nomeJogador = str(input('Nome do jogador: ')).upper()
numeroGols = str(input(f'Número de Gols do jogador {nomeJogador}: '))
if numeroGols.isnumeric():
    numeroGols = int(numeroGols)
else:
    numeroGols = 0
if nomeJogador.strip() == '':
    ficha(gols=numeroGols)
else:
    ficha(nomeJogador, numeroGols)
