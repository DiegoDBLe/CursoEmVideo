n = s = c = 0
while c <= 5:
    n = int(input('Digite o numero: '))
    c += 1
    if n == 999:
        break
    s += n
print(f'A soma é {s}') # F STRING

while c <= 10:
    print(c, '->', end='')
    c += 1
print('ACABOU')

