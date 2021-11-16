# FAÇA UMA PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA notas() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
# QUANTIDADE DE NOTAS; A MAIOR NOTA; A MENOR NOTA; A MÉDIA DA TURMA; A SITUAÇÃO(OPCIONAL). ADICIONE TAMBEM AS DOCSTRINGS DA FUNÇÃO.
def notas(*n, situ=False):
    '''
    -> Função que recebe varias notas e mostra a situação de acordo com a média
    :param n: variável que recebe várias notas.
    :param situ: situação que quando selecionado True mostra situação do aluno de acordo com a média: BOA, RUIM ou RAZOÁVEL
    :return: retorna o calculo das notas.
    '''
    r = dict()
    r['Total'] = len(n) # Total de notas passadas
    r['Maior Nota'] = max(n) # Maior nota
    r['Menor Nota'] = min(n) # menor nota
    r['Média'] = sum(n) / len(n) # média
    if situ:
        if r['Média'] >= 7:
         r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


#Programa Principal
resultado = notas(7.8, 2.8, 1.7, situ=True)
print(resultado)

