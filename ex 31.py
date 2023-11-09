distancia =  int (input('Qual a distancia(KM) da sua viagem ?'))

if distancia <= 200 :
    valoPassagem = 0.5 * distancia
    print(f'Valor da sua passagem sera de R${valoPassagem:,.2f} ') 
else:  
    valoPassagem = 0.45 * distancia
    print(f'Valor da sua passagem sera de R${valoPassagem:,.2f} ')