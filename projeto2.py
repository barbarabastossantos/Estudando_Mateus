tempo=int(input('quantos anos tem o seu carro?  '))
#tempo é minha variavel, int é o tipo da minha variavel o tipo inteiro, input é um comando de entrada  para o usuario interagir.

if tempo <= 3:
    #if é nosso estrutura condicional simples se, tempo é nossa variavel é a condição é  : se o tempo for menor ou iigual a três  ou seja essa bloco é verdadeiro True  escreva carro novo
    #outro ponto que quero chamar  atenção  tanto no final do if quanto do else tem que por dois pontos no final deles
    print('carro novo')
else:
    #o else faz parte da estrutura condicional composta if/else (se/entao) , se o bloco do if não for verdadeiro entao (else) execute esse bloco o bloco do else imprimindo carro velho
    print('carro velho')
print('-------------fim------------------')

