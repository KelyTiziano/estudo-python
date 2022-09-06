from random import randint

jogador=input(f"jogador, escolha par ou impar ")
jogador=int(input(f"escolha um número de 0 a 10 "))
computador=randint(1,10)
print(f"computador escolheu {computador}")
total=jogador+computador
print(f"total {total}")
par=total%2

if par==0:
    print(f"vence par")
else:
    print(f"vence impar")

#não rodou, deu erro: invalid syntax, tambpem estou com duvida sobre o que signofoca esse%2. tentei tirar duvida em exercicio anterior mais não consegui



