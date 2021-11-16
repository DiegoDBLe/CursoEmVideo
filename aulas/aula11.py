# Condições Aninhada: varias maneiras de representar 
nome = str(input('Digite seu nome: '))
if nome == 'Diego':
    print('Nome Bonito')
elif nome == 'Levi' or nome == 'Mauro' or nome == 'Sergio':
    print('Nome Muito Forte')
elif nome in 'Patricia Thyci Marina Lucia':
    print('Nome Feminino')
else:
    print('Seu nome é tão normal!')
print('Tenha um Bom Dia, {}!'.format(nome))
