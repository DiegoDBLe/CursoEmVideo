# CRIE UM PROGRAMA QUE TENHA UM FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E O OUTRO CHAMADO SHOW, QUE SERÁ UM
# VALOR LÓGICO(OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CÁLCULO DO FATORIAL.
def fatorial(n, show=False):
    '''
    fatorial(n, show=False)
    -> Calcule o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(int(input('Digite um número: ')), show=True))
help(fatorial)

