# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python
# de uma forma simples.

# Tratamento de Exceção:
# try: (tente)
# - operação que normalmente dar problema.
# except:
# - tratamento da exceção.

# Erro de divisão por zero:     ZeroDivisionError: division by zero
try: # tente
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except: # se der problema
    print(f'Infezlimente tivemos um problema :(')

else: # se não der problema. ou seja deu certo o try
    print(f'O resultado é {r:.1f}')

finally: # a calsula finally vai acontecer se deu certo ou não ela sempre que invocada acontece.
    print('Volte Sempre! Muito Obrigado!')

print()
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
print()
# Mesmo teste do de cima porém agora  além de mostrar a msg mostra o tipo de erro atraves da classe Exception.
try: # tente
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro: # se der problema
    print(f'Infezlimente tivemos um problema :( e o problema foi ({erro.__class__})')

else: # se não der problema. ou seja deu certo o try
    print(f'O resultado é {r:.1f}')

finally: # a calsula finally vai acontecer se deu certo ou não ela sempre que invocada acontece.
    print('Volte Sempre! Muito Obrigado!')

print()
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
print()

# Tratando vários tipos de erros especificos:
try: # tente
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError): # Se for erro de valor e erro de tipo vai mostrar uma mensagem especifica:
    print(f'Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')

except KeyboardInterrupt:
    print('Usúario preferiu não informar os dados.')

else: # se não der problema. ou seja deu certo o try
    print(f'O resultado é {r:.1f}')

finally: # a calsula finally vai acontecer se deu certo ou não ela sempre que invocada acontece.
    print('Volte Sempre! Muito Obrigado!')
