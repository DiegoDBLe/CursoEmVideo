# CRIANDO UM PROGRAMA DE CONTROLE DE ACESSO
print('~=~' * 30)
print(' ' * 30, 'CONTROLE DE ACESSO!')
print('~=~' * 30)
tentativa = c = 1
while True:
    tentativa = str(input(f'Digite sua senha {c}° Tentativa: ')).strip()
    c += 1
    if tentativa != '180288@@':
        print('\033[1;31mSenha Inválida!\033[m')
    if tentativa == '180288@@':
        print('\033[1;32mAcesso liberado!\033[m')
        break
    elif c >= 4:
        print('~=~' * 30)
        print('\033[1;31mAcesso Negado!\033[m')
        break
print(f'Foram feitas {c - 1} tentativas.')
