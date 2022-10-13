nota1=float(input("digite a primeira nota" ))
nota2=float(input("dogite a segunda nota"))
media=(nota1+nota2)/2

if media >=9<=10:
    print(f"sua média é {media} nota A, 'APROVADO' ")
elif media >=7.5<9:
    print(f"sua média é {media} nota B, 'APROVADO' ")
elif media >=6<7.5:
    print(f"sua média é {media} nota C, 'APROVADO' ")
elif media >=4<6:
    print(f"sua média é {media} nota D, 'REPROVADO' ")
elif media >=0<4:
    print(f"sua média é {media} nota E, 'REPROVADO' ")
