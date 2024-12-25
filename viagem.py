print('= *30')
print('          CALCULANDO  O CUSTO DA SUA VIAGEM')
print('='*30)
n=input('Qual é o seu nome ?  ')
print(f' Que bom ter você aqui {n} ! Vamos agora calcular o preço da sua passagem. Vamos lá!')
d=float(input('Precisamos saber a distancia do seu distino em km. \n  Digite quantos Km tem seu distino : '))
if d<= 200:
    print(f' {n} , seu custo será de R$  { (d *0.50 ):.2f}')
else:
    print(f' {n} seu custo  será de R$ { ( d * 0.45  ):.2f} ')