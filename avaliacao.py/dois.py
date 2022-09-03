from random import randint

jog=input("jogador escolha uma opcao,pedra,papel ou tesoura? ")
computer=randint("pedra,papel,tesoura ")
if jog==computer:
    print(f"empate")

if jog=="pedra" and computer=="tesoura":
    print(f"vence jogador ")
elif computer=="papel":
    print(f"vence computer ")
    if computer=="pedra" and jog=="tesoura":
        print(f"vence computer")
    elif jog=="papel":
        print(f"vence jogador")

#esse aqui também não consegui fazer rodar, somente a primeira interação com jogador. Não sei como fazer o parentese desse randint
