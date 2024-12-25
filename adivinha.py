print('=' *30)
print('=========         VAMOS JOGAR?          ========')
print('=' *30)
nome=input('Jogador qual é o seu nome? ')
print(f'    Que bom ter você aqui  na Bastos Game  {nome}, nosso jogo é na verdade um desafio para você! \n  Te desafiamos a acertar  qual é o numero que a Julia esta pensando. \n DICA: É um numero entre 0 e 10 ')
print("=" *30)
s=input(f'Eai , {nome} topa nosso desafio? ') .strip() .upper()
if s== "SIM":
    print("=" *30)
    print('         CARREGANDO . . . ')
    print('='*30)
    n=int(input(f' Vamos lá !  {nome} qual é o numero que a julia pensou?   '))
    if n == 7 :
        print(f' Uaau!! Você acertou {nome},  incrivel ! Parabens! ')
        print(f'=====     {nome} VENCEU!!!      ===== ')
        print('=' *30)
    else:
        print(f"  {nome} , não foi dessa vez. ")
        print('='*30)
else:
    print(f" {nome} , quando estiver afin ficaremos felizes em ter você aqui conosco jogando.")
    print('='*30)