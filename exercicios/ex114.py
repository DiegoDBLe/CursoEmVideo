# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu Erro!')
else:
    print('Deu certo!')

# Comando para pegar os códigos(conteudo) html da pagina:
    print(site.read())
