# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITA UMA EXPRESSÃO QUALQUER QUE USE PARENTESES. SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARENTESES
# ABERTOS E FECHADOS NA ORDEM CORRETA.
expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
