# Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição (sem usar o sort) no final mostre
# a lista ordenada na tela:
listaNumber = list()
for c in range(0, 5):
   number = int(input('Enter a number: '))
   if c == 0 or number > listaNumber[-1]:
      listaNumber.append(number)
      print('Number added to end of list')
   else:
      pos = 0
      while pos < len(listaNumber):
         if number < listaNumber[pos]:
            listaNumber.insert(pos, number)
            print(f'Number insert in position {pos}° the list...')
            break
         pos += 1
print('-=-' * 30)
print(f'The values entered were: {listaNumber}')
