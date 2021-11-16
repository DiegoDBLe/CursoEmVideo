# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UM LISTA. Depois disso mostre: A) Quantos numeros foram digitados; B) A lista de forma decrescente
# C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LSTA.
lista = list()
c = 0
while True:
    lista.append(int(input('Digite um número: ')))
    c += 1
    print('Número adicionado com sucesso!')
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resposta in 'Nn':
        break
lista.sort(reverse=True)
print(f'- Quantos numeros foram digitados: {c}') # ou print(f'- Quantos numeros foram digitados: {len(lista)}')
print('- A lista de forma decrescente {}'.format(lista))
if 5 in lista:
    print('- O número 5 está na lista.')
else:
    print('- O número 5 não está na lista')
