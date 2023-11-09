import time

print('_'*50)
print('Digite tres numeros para sabermos qual é o maior.')
#time.sleep(2)
print('_'*50)
primeiro= int(input('Informe o primeiro numero:'))
segundo= int(input('Informe o segundo numero:'))
terceiro=int(input('Informe o tercei nroumero:'))
print ('Verificando qual o maior')
#time.sleep(5)
if primeiro > segundo & primeiro > terceiro:
    print(f'O numero {primeiro} é o maior ente os tres')
else:
    if segundo > terceiro:
        print(f'O numero {segundo} é o maior entre os tres')
    else:
        print(f'O numero {terceiro} é o maior entre os tres')