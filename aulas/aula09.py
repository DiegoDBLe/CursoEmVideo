#MANIPULANDO TEXTOS

frase = 'Curso Em Video'
print('Quantas letras tem a frase?: ', len(frase))
print('Fatiando por letra:', frase[3])
print('Fatiando de letra até outra letra:', frase[3:11])
print('Inicio ate a letra que eu definir:', frase[:12])
print('Do inicio até o fim pulando de 2 em 2: ', frase[1:12:2])
print('Do inicio até o fim pulando de 2 em 2:',frase[::2])
print('Quantas vezes aparece a letra o: ', frase.count('o'))
print('Quantas vezes aparece a letra o: ', frase.upper().count('O'))
print('QEm qual posição começa a palavra deo. Na posição: ', frase.find('deo'))
print('Posição da palavra Python: ', frase.find('Python'))
print('Exista a palavra Python na frase?: ', 'Python' in frase)
print('Adicionar uma palavra na frase ou alterar: ', frase.replace('Em', 'Python'))
print('Deixar todas as letras da frase em MAIUSCULA: ', frase.upper())
print('Deixar todas as letras da frase em minuscula: ', frase.lower())
print('Somente a primeira Letra em Maiusculo: ', frase.capitalize())
print('Deixar todas as letras do inicio da frase em MAIUSCULA: ', frase.title())
print('Remove os espaços antes da string: ', frase.strip())
print('Remove os espaços da direita da string. Ou seja os ultimos espaços: ', frase.rstrip())
print('Remove os espaços da esquerda da string. Ou seja os espaços do inico: ', frase.lstrip())
print('Divide os indices das string:', frase.strip())
print('-'.join(frase))
