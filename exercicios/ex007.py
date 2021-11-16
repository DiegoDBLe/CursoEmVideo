#FAÇA UM PROGRAMA QUE LEIA QUANTO DINEHIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES
# U$$ 1,00 VALENDO R$ 5,25 cotação 05/06/2021
# EURO R$ 6,21
# LIBRA R$ 7,31
real = float(input('Quantos reais você tem? R$'))
dolar = real / 5.25
euro = real / 6.21
libra = real / 7.21
iene  = real / 20.93
bitcoin = real / 0.0000047
bolivarVenezuelano = real * 768.731
pesoArgentino = real * 18.45
pesoChileno = real * 148.28

print('Tranformando em dolares você possui: UU$ {:.2f} \n Euro {:.2f} \n Libra {:.2f} \n Iene {:.2f} \n Bitcoin {:.2f} '
      '\n Bolivar Venezeuelano {:.2f} \n Peso Argentino {:.2f} \n Peso Chileno {:.2f}'
      .format(dolar, euro, libra, iene, bitcoin, bolivarVenezuelano, pesoArgentino, pesoChileno))
