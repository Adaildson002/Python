texto = str(input('Digite o texto:')).upper().strip()

print('A letra A aparece {} vezes no texto'.format(texto.count('A')))
print('A prineira posição que A aparece é {}'.format(texto.find('A')+1))
print('E a Ultima posção é {}'.format(texto.rfind('A')+1))