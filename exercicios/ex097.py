# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBA UM TEXTO QUALQUER COMO PARAMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTAVÉL.
def escreva(msg):
    tam = len(msg)
    for letra in msg:
        print('-', end='')
    print()
    print(msg)
    for letra in msg:
        print('-', end='')
    print()


escreva('Curso em Video')
escreva('Diego Dantas Batista')
escreva('OI')


# SOLUÇÃO DO PROFESSOR:
def palavra(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)


palavra('Diego Dantas Batsista')
palavra('Levi')
palavra('Oi')
