from random import randint
computador = randint(0,5)
print('Pensei em um numero de 0 a 5 tente adivinhar')
jogador = int ( input ( 'Em que numero eu pensei?'))
                  
if computador == jogador:
    print('Voce acertou' )
    
else:
    print('Voce Errou, eu pensei no {}').format (computador)   

