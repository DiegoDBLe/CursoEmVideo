#Escreva um programa que pergunte o sálario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R$ 1.250,00, calcule aumento de 10%
#Para os inferiores ou iguais o aumento é de 15%
nome = str(input('Digite o nome do Funcionário:'))
salario = float(input('Qual o Salário do Sr(a).{} R$ '.format(nome)))
if salario >= 1250:
    aumento = (salario * 10) / 100
    novoSalario = salario + aumento
    print('Seu salário é R$ {:.2f} reais com aumento de 10% R$ {:.2f} reais o salário do Sr(a).{} ficará: R$ {:.2f} reais'.format(salario, aumento, nome, novoSalario))
else:
    aumento = (salario * 15) / 100
    novoSalario = salario + aumento
    print('Seu salário é R$ {:.2f} reais com aumento de 15% R$ {:.2f} reais o salário do Sr(a).{} ficará: R$ {:.2f} reais'.format(salario,aumento, nome, novoSalario))
