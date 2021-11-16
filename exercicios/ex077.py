# CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (não usar acentos). DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO SUAS VOGAIS:
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
# esse primeiro for vai analisar cada elemento(palavra) da tupla.
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p: # esse for vai pegar cada elemnto da tupla
        if letra.lower() in 'aeiou': # e aqui no if vai analisar se tem as vogais em cada elemento da tupla
            print(letra, end=' ') # as que tiver vai ser printada
