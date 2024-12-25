print('======================================================')
print('====================MÉDIA DO SEMESTRE====================')
print('======================================================')
#esses tres primeiros prints foram  uma especi de   layout  simples para meu programa para melhorar um pouco a esperiencia do meu usuario
#esse primeiro print e o ultimo sao linhas decorativas. eu fiz desse jeito mas poderia ser  print("=" *30)
#o print do meio que tem meu titulo do programa  eu fiz assim mas poderia ter sido  assim  print("=====             MEDIA  DO SEMESTRE        =====")
nome=input('Ola aluno! Qual é seu nome : ')
#Variavel nome , como eu omiti o tipo ele subentende que e string
n1=float(input('Digite su nota da primeira prova : '))
n2=float(input('Digite sua nota da segudanda prova :  '))
n3=float(input('Por fim digite sua nota da terceira  prova : '))
#as variaveis n1 n2 n3 sao do tipo real , float
m=float (n1+n2+n3)/3
#nossa variavel media  e do tipo float
# o calculo da media precisamos usar o principio da precedencia  pois queremos que a soma seja feita primeiro e so depois a divisão para isso usamos o recurso do parenteses
print('=====================================================')
print('                   V E R I F I C A N D O . . .  ')
#mais um tipo de layout  pra fazer uma graça com meu usuario kkkk
if m >=6 :
    #aqui entramos  na nossa estrutura condicional
    # if o nosso se   a media for maior ou igual a seis nosso primeiro bloco e verdadeiro, entao vai ser imprimido a messagem parabenizando
    print(f'          PARABENS!!!!  {nome} , você alcançou a media para a aprovação {m :.1f} \n  Que o proximo semestre você continue evoluindo!\n  Nois da instituição de ensino Bastos estamos aqui  sempre para contribuir com o seu sucesso! ')
else:
    #else nosso senao se o bloco for falso vamos printar  essa messagem de reprovação
    print(f'   NÃO FOI DESSE VEZ. {nome} , você não alcançou a media minima para a aprovação , sua media foi  {m:.1f} \n   Que no proximo semestre  você  possa evoluir  e alcançar notas melhores. \n Se precisar de ajuda em algo estamos a sua disposição! \n Nois da instituição de ensino Bastos estamos aqui sempre para contribuir com o seu sucesso! ')
#nesses prints usei a formatação f f' colado nas aspas mas do lado de fora  pra poder por as chaves com minhas variaveis {m}  e tambem coloquei na variavel a formatacao pra so ter uma casa decimal depois da virgula {m:.1f} e quebrei linhas \n
print('=============================================================')
print('=============================================================')
#mais uma graça visual para meu usuario kkk