nome=input(' Qual é o seu nome ?  ').strip() .lower()
#variavel nome
# , input e comando de entrada ,
# .strip() serve para tirar os espaços que o usuario por,  .lower() para colocar tudo em letra  minusculas, e se quiser tudo em maiuscula coloca  . upper()
if nome == 'barbara':
    #estrutura condicional simples  if  o nosso se do pseudocodigo
    # a igualdade no python e o ==,
    # nosso teste logico nesse caso a stringo "barbara' entre aspas  pq se nao estiver o programa acha que e uma variavel
    print( f' Que nome lindissimo {nome}')
    #esse print so vai imprimir  se a condiçao if for verdadeira se for falsa não imprime pois faz parte da condição if
print('Bom dia ! Você é uma pesssoa incrivel!')
#essse print vai imprimir independente se a condição for verdadeira ou falsa  pois está fora da condição if