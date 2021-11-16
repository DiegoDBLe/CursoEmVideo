# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA. MAS SÓ ACEITE OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO
#Minha solução
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo: [F/M] : ')).strip().upper()[0]
print('FIM')

# SOLUÇÃO PROFESSOR:
sexo = str(input('Digite seu sexo: [F/M] : ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[1;31m[ERROR] DADOS INVÁLIDOS\033[m.Digite seu sexo novamente: [F/M] : ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
