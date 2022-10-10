nota1=float(input("digite a primeira nota"))
nota2=float(input("digite a segunda nota"))
media=(nota1+nota2)/2
if media ==7:
    print(f"nota {media} aprovado com distinção")
elif media >=7:
    print(f"nota {media} aprovado")
else:
    print(f"nota {media} reprovado")
