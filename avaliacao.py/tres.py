nota1=int(input("nota prova 1 "))
nota2=int(input("nota prova 2 "))
nota3=int(input("nota trabalho final "))
media=(nota1+nota2+nota3)/3
print(f"media final ficou em {media}")

if media >= 7:
    print(f" nota igual ou maior que a media, PARABÉNS VOCê PASSOU DIRETO")
if media>=5 and media<=7:
    print(f"nota menor do que a media, ATENÇÃO VOCÊ ESTÁ EM RECUPERAÇÃO ")
if media <= 5:
    print(f"nota muito baixa sem recuperação, VOCÊ FOI REPROVADO")

#it's correct, but when to use "float"?
#line 9 was wrong
