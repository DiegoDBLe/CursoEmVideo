val = list(range(1, 5))
print(val)

pontos = (1,10,8,7,2,4,3)
print(sorted(pontos))


def teste(a, b=1, c=2):
    soma = a + b + c
    return soma


print(teste(1, 2, 3))

num = [3, 6, 4, 1]
for n1, n2 in enumerate(num):
    print(n1 + n2, end='')

print()
letras = ('J', 'X', 'M', 'O', 'A', 'K')
print(letras.index('A'))
print()

num = [6, 2, 1, 4, 3]
num.sort(reverse=True)
print(num)
print()

pessoas = [['Pedro', 25], ['Maria', 12], ['José', 25]]
print(pessoas[2][1])
print()

num = [2, 8, 4, 7]
num.pop()
num.insert(1, 3)
num.append(6)
print(num)
print()

print()
# a = 3
#
# b = a * 2
#
# a, b = b, a
#
# print(a)
print()
print()

a = 0
for i in range(30):
   if a%2 == 0:
     a += 1
     continue
   else:
     if a%5 == 0:
        break
     else:
        a += 3
print(a)