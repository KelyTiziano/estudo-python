jogador_1=int(input("escolha um numero de 0 a 10"))
jogador_2=int(input("escolha um numero de 0 a 10"))
resultado=jogador_1+jogador_2
talvez_par=resultado%2
if talvez_par==0:
    print(f"o jogador venceu")
else:
    print(f"o jogador perdeu")


