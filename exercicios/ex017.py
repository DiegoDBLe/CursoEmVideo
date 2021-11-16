# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
# na tela o nome do escolhido.
import random
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome:  ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome:   ')
nome5 = input('Digite o quinto nome:   ')
nome6 = input('Digite o sexto nome:    ')
nome7 = input('Digite o setimo nome:   ')
nome8 = input('Digite o oitavo nome:   ')
nome9 = input('Digite o nono nome:     ')
nome10 = input('Digite o decimo nome:  ')
lista = [nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8, nome9, nome10]
escolhido = random.choice(lista)
print('O Escolhido foi {}'.format(escolhido))
