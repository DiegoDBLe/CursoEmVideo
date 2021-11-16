#Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
#o uso de docstrings para documentar nossas funções,argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
# Interactive Help( Ajuda Interativa):
#help(print) # Comando para acessar a descrição da função ou seja mostra os parametros do comando print, as informações de qualquer função padrão do Python

# DOCSTRINGS => ( Para descrever a função que você criou), atráves do DOCSTRINGS registra-se as informações da função criada
#EX:

# Def de msg padronizada:
def print_modificado(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


def contador(i, f, p):
    # Abaixo exemplo de DOCSTRINGS OU SEJA DOCUMENTANDO O PASSO A PASSO DA FUNÇÃO
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)
print()
print()
print('-=' * 30)

# ABAIXO PARÂMETROS OPCIONAIS:


def somar(a, b, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: Valor da soma de tres numeros
    OBS: parametro opcional é quando declaro 3 parametros e passo somente 2. No terceiro parametro digo que recebe c=0. Assim posso passar
    somente dois parametros e o programa funcionar normalmente.
    """
    s = a + b + c
    print(f'A soma é {s}')


somar(5, 6)

print()
print()
print('-=' * 30)

# ABAIXO ESCOPO DE VARIÁVEIS: Local onde varivael vai começar a existir e onde morre.


def teste():
    x = 8 # Variável de escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2 # Variável de escopo Global
print(f'Na função teste, n vale {n}')
teste()
#print(f'Na função teste, x vale {x}') # Não vai funcionar pois a váriavel x pertence somente a def teste

print()
print()
print('-=' * 30)

# Mais um exemplo:
n1 = 2
print(f'N1 de fora vale {n1}')


def funcao():
    global n1
    n1 = 4
    print(f'N1 de dentro vale {n1}')


funcao()
print(f'N1 mudou e agora vale: {n1}')

print()
print()
print('-=' * 30)

# RETURN DE VALORES EM DEF. -> Quando uma def vai retornar o a função da função. Se for somar tres numeros ela vai retornar o resultado de tres numeros


def soma(a, b, c=0):
    s = a + b + c
    return s


s1 = soma(2, 5, 3)
s2 = soma(2, 2)
print(f'Os resultados fora {s1} e {s2}')
print()
print()
print('-=' * 30)

# FATORIAL:


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2}, e {f3}')

print()
print()
print('-=' * 30)


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É Par')
else:
    print('É Impar')
