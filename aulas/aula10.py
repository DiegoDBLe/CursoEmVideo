#COLOCANDO CORES NO TERMINAL E NOS CÓDIGOS
# \033[style;text;backgroud m
# códigos do style: 0 (none ou seja nada), 1(Bold ou seja negrito) 4(Underline) 7(Ao contrário ou seja fundo da cor contraria)
# códigos do text: vai do 30 até 37 (30 (Branco) - 31 (Vermelho) - 32 (Verde) - 33 (Amarelo) - 34 (Azul) - 35 (Roxo) - 36 (azul bebe)  - 37 (Cinza)
# códigos do backgroud vai de 40 até 47 mesma sequencia do text

print('\033[31mOlá mundo em Vermelho!')
print('\033[32;4mOlá mundo em Verde e Underline')
print('\033[33;1mOlá Mundo em Amarelo e Negrito')
print('\033[34;7;40mOlá Mundo em Azul e fundo ao contrario')
print('\033[4;33;47mOlá Mundo Sublinhado e marca texto ate o final da frase!\033[m')

# OUTRA MANEIRA
nome = 'Diego'
print('Muito prazer Sr.{}{}{} !!!'.format('\033[1;31m', nome, '\033[m'))
