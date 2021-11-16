#FAÇA UM PROGRAMA QUE MOSTRE O SALARIO DE UM FUNCIONARIO E SOME COM AUMENTO DE 15%
salario = float(input('Qual o salario do funcionario? R$ '))
novoSalario = salario + (salario * 15 / 100)
print('O Funcionario que ganhava R$ {:.2f}, com aumento de 15% passa a aganhar R$ {:.2f} '.format(salario, novoSalario))
