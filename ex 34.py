salario = float(input('Qual o seu salario:  '))

if salario <= 1250:
    salario = salario + (salario*(15/100))
else:
    salario = salario +(salario*(10/100))

print (f'Seu novo salario sera de {salario:.2f}')