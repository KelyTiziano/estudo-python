from random import randint
jogador_1=int(input(" jogador 1isaac escolha um numero de 0 a 10 "))
computer=randint(1,10)
resultado=jogador_1+computer
talvez_par=resultado%2
if talvez_par==0:
    print(f"o jogador escolheu {jogador_1}")
    print(f"the computer choose {computer}")


