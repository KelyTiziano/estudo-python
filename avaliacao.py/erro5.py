from random import randint

humano = int(input("Escolha: 1 - pedra, 2 - papel, 3 - tesoura"))
print(f"voce escolheu {humano}")
opcao_humano=humano

computador = randint(1,3)
print(f"computador escolheu {computador}")

if humano == 1:
    opcao_humano = "pedra"
elif humano == 2:
    opcao_humano = "papel"
elif humano == 3:
    opcao_humano = "tesoura"
else:
    print("Voce escolheu uma opcao invalida")

if computador == 1:
    opcao_computador = "pedra"
elif humano == 2:
    opcao_computador = "papel"
elif humano == 3:
    opcao_computador = "tesoura"

print(f"Voce escolheu {opcao_humano} e o computador escolheu {opcao_computador}")
print(f"Quem ganha?")

#faltava o comando:  from random import randint
#faltava : em alguns dos elifs e no else
#coloquei dois sinais de == em todos que havia apenas 1 =, fiquei na duvida se realemnte isso teria sido um erro.
#na primeira variavel havia um print, eu coloquei um input com int, por se tratar de uma interaçãocom o usuario e fiquei meio na duvida quanto ao int, mas como havia numero eu resolvi colocar
#a variavel opcao_humano não existia
#fiz o print da escolha do computador e do humano também
#PERGUNTA: os ultimos elifs em relação a escolha dos "variantes" poderiaser apenas else?
