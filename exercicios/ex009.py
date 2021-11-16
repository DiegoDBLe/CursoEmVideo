# FAÇA UM PROGRAMA QUE LEIA A LARGURA E ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE
# DE TINTA NECESSARIA PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2m²:

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede você precisa de {}Lts de tinta.'.format(tinta))
