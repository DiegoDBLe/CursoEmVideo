# def(funções) em python. O que é função? é um Rotina. ou seja uma coisa que você faz constantemente.
# EXEMPLO DE DER SEM PARAMETRO:


def mostraLinha():
    print('-' * 30)


mostraLinha()
print('     Sistema de Aluno        ')
mostraLinha()
print('     Sistema de Funcionário        ')
mostraLinha()
print('     Sistema de Aulas        ')
mostraLinha()


def espaco():
    print()
    print('-=' * 30)
    print()


espaco()


# EXEMPLO DE DEF COM PARAMETRO:
def mensagem(msg):
    print('-' * 30)
    print(f'    {msg}    ')
    print('-' * 30)


mensagem('Sistema de Aluno')
mensagem('Sistema de Funcionário')
mensagem('Sistema de Aulas')

espaco()


mensagem('FUNÇÃO SOMAR DOIS PARAMETROS:')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(int(input('Digite um numero: ')), int(input('Digite outro numero: ')))
soma(15, 2)

espaco()

# EXEMPLO DE DEF COM VÁRIOS PARAMETROS:
mensagem('FUNÇÃO COM VÁRIOS PARAMETROS(EMPACOTAMENTO) : ')


def contador(* num):
    # Vai gerar uma tupla:
    print(num)
    tam = len(num)
    for valor in num:
        print(f'{valor} ', end='')
    print('- FIM')
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(1, 2, 3)
contador(4, 5, 6, 7, 8, 9)
contador(10)
contador(int(input('Digite um numero: ')), int(input('Digite outro valor: ')), int(input('Outro valor: ')))

espaco()

# PASSANDO LISTA COMO PARAMETRO DE UMA DEF: Não passo direto uma lista e sim chamo a def e passo como paramentro a lista
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Valores: {valores}')


def dobraValor(lista):
    pos = 0
    while pos <len(lista):
        lista[pos]*= 2
        pos += 1


dobraValor(valores)
print(f'Dobrando os valores da lista: {valores}')



