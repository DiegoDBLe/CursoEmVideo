# MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.
print('Gerador de PA')
print('=' * 20)
primeiro = int(input('Digite o primeiro termo: ')) #Numero que vai começar a contar
razao = int(input('Digite a Razão da PA: ')) #pular de quantos em quantos
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))


