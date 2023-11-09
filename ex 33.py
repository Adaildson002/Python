import time

print('_'*50)
print('Digite tres numeros para sabermos qual é o maior e menor.')
time.sleep(2)
print('_'*50)

# Recebe os tres numeros infomados
primeiro = int(input('Informe o primeiro numero:'))
segundo = int(input('Informe o segundo numero:'))
terceiro = int(input('Informe o tercei numero:'))

print ('VERIFICANDO QUAL O MAIOR E O MENOR . . .')

# verifica se todos são iguais, se não damos inicio a verificação do maior
if primeiro==segundo and primeiro == terceiro:
    print('TODOS OS NUMEROS SÃO IGUAIS')
else:
    if primeiro > segundo and primeiro > terceiro:
        print(f'O numero {primeiro} é o maior')
    else:
        if segundo > terceiro:
            print(f'O numero {segundo} é o maior')
        else:
            print(f'O numero {terceiro} é o maior')

# verifica se todos são iguais, se não damos inicio a verificação do menor
if primeiro==segundo and primeiro == terceiro:
    print ('')
else:
    if primeiro < segundo and primeiro < terceiro:
        print(f'O numero {primeiro} é o menor')
    else:
        if  segundo < terceiro:
            print(f'O numero {segundo} é o menor')
        else:
            print(f'O numero {terceiro} é o menor')
