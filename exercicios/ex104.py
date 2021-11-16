# CRIE UM PROGRAMA QUE TENHA A FUNÇÃO leiaInt(), QUE VAI FUNCIONAR DE FORMA SEMELHANTE À FUNÇÃO input() DO PYTHON, SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR
# APENAS UM VALOR NUMÉRICO
def leiaInt(msg):
    ok = False
    valor = tentativa = 0
    while True:
        tentativa += 1
        if tentativa >= 11:
            print('\033[1;31m[ERROR]Você atingiu a quantidade máxima de tentativas.\033[m')
            break
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print(f'\033[0;31mERROR! Digite um número válido! {tentativa}° tentativa de 10.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'O valor digitado foi {n}')
