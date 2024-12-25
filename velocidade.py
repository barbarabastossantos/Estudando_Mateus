print('=' *30)
print('                 RADAR DE VELOCIDADE ')
print('='*30)
print(' Acidentes nas estradas tem ceifados muitas vidas !\n No transito tenha conciência dirija com respeito  e responsabilidade. \n         SALVE VIDAS!!!!!')
v=int(input('Qual é a  sua velocidade na BR  166  em KM/h  :  '))
m= (v-80) *7
if v > 80 :
    print('                     ALERTA !!!!!!!!!!!!!!')
    print(f'Você ultrapassou a velocidade permitida de 80 km/h  sua multa sera de R$  {m} ,00 pois são R$ 7,00 por km ultrapassado  \n TENHA MAIS RESPONSABILIDADE !')
else:
    print('     PARABENS! Sua velocidade esta dentro do limite')