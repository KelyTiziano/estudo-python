from random import randint

jog=input("jogador escolha uma opcao,pedra,papel ou tesoura? ")
computer=randint(1,3)
if computer==1:
    computer="pedra'"
elif computer==2:
    computer="papel"
else:
    computer="tesoura"

if jog==computer:
    print(f"empate")

if jog=="pedra" and computer=="tesoura":
    print(f"vence jogador ")
else:
        print(f"vence computer")
if jog=="pedra" and computer=="papel":
    print(f"vence computer ")
else:
        print(f"vence jogador")
if jog=="tesoura" and computer=="pedra":
        print(f"vence computer")
else:
        print(f"vence jogador")

#esse aqui também não consegui fazer rodar, somente a primeira interação com jogador. Não sei como fazer o parentese desse randint
