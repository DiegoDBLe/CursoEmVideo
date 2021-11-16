# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS:
media = float(input('Digite uma Distância em metros: '))
c = media * 100
m = media * 1000
k = media * 0.001
mc = media * 1e+6
nm = media * 1e+9
milhas = media * 0.000621371
jarda  = media * 1.09361
pé = media * 3.28084
polegada = media * 39.3701
milhasNautica = media * 0.000539957
print('A média de {}m corresponde a \n{:.0f} cm  \n{:.0f} mm \n{} km \n{} micrômetro \n{} nanômetro '
      '\n{:.3f} Milhas \n{:.3f} Jardas \n{} Pés  \n{} Polegadas \n{} Milhas Nauticas'
      .format(media, c, m, k, mc, nm, milhas, jarda, pé, polegada, milhasNautica))



