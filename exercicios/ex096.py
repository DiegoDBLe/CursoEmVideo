# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR(LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.
def mensagem(txt):
    print('-' * 30)
    print(f'    {txt}   ')
    print('-' * 30)


mensagem('CONTROLE DE TERRENOS')


def terreno(largura, comprimento):
    areaTotal = largura * comprimento
    print(f'A área total do terreno {largura} x {comprimento} é de {areaTotal}m². ')


terreno(float(input('LARGURA (m²): ')), float(input('COMPRIMENTO (m²): ')))
