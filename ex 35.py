print ('Informe 3 compreimentos para saber se formam um triangulo')

compr1 = float(input("primeiro comprimento"))
compr2 = float(input('segundo comprimento'))
compr3 = float(input('terceiro comprimento'))

if compr1 < compr2 + compr3 and compr2 < compr1 + compr3 and compr3 < compr1 + compr2:
    print('Esses comprimentos podem formar um TRIANGULO')
else:
    print('Esses comprimentos nao podem formar um TRIANGULO')